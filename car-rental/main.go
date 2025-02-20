package main

import (
	"context"
	"database/sql"
	"flag"
	"fmt"
	"log"
	"net"
	"time"

	"github.com/google/uuid"
	_ "github.com/mattn/go-sqlite3"
	"github.com/thihxm/car-rental/internal/config"
	"github.com/thihxm/car-rental/internal/database"
	base "github.com/thihxm/car-rental/protos/base"
	pb "github.com/thihxm/car-rental/protos/car-rental"
	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 50054, "The server port")
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	pb.UnsafeCarRentalServiceServer
	cfg *config.ApiConfig
}

func findAvailableCar(cfg *config.ApiConfig, requiredSeats int32, location string, checkInDate time.Time, checkOutDate *time.Time) (*database.Car, error) {
	var endDate sql.NullTime
	if checkOutDate != nil {
		endDate = sql.NullTime{Time: *checkOutDate, Valid: true}
	}

	car, err := cfg.Queries.GetFirstAvailableCar(context.Background(), database.GetFirstAvailableCarParams{
		Location:  location,
		Seats:     int64(requiredSeats),
		StartDate: checkInDate,
		EndDate:   endDate,
	})
	if err != nil {
		return nil, err
	}
	return &car, nil
}

func (s *server) RentCar(_ context.Context, in *base.CreateReservationRequest) (*base.CreateReservationResponse, error) {
	log.Printf("Received: %v", in.GetCheckInDate())
	var success = true
	var message = "Car rented successfully"

	var checkOutDate *time.Time
	if in.GetCheckOutDate() != nil {
		parsedCheckOutDate := in.GetCheckOutDate().AsTime()
		checkOutDate = &parsedCheckOutDate
	}

	car, err := findAvailableCar(s.cfg, in.GetNumberOfPeople(), in.GetDestination(), in.GetCheckInDate().AsTime(), checkOutDate)
	if err != nil {
		success = false
		message = "Nenhum carro disponível para a data selecionada"

		var responseBuilder = base.CreateReservationResponse_builder{
			Success: success,
			Message: message,
		}
		return responseBuilder.Build(), nil
	}

	var endDate sql.NullTime
	if checkOutDate != nil {
		endDate = sql.NullTime{Time: *checkOutDate, Valid: true}
	}

	reservation, err := s.cfg.Queries.CreateReservation(context.Background(), database.CreateReservationParams{
		ID:        uuid.New().String(),
		CarID:     car.ID,
		StartDate: in.GetCheckInDate().AsTime(),
		EndDate:   endDate,
	})

	if err != nil {
		success = false
		message = "Não foi possível criar a reserva"

		var responseBuilder = base.CreateReservationResponse_builder{
			Success: success,
			Message: message,
		}
		return responseBuilder.Build(), nil
	}

	var responseBuilder = base.CreateReservationResponse_builder{
		Success:       success,
		Message:       message,
		ReservationId: &reservation.ID,
	}
	return responseBuilder.Build(), nil
}

func main() {
	db, err := sql.Open("sqlite3", "./car-rental.db")
	if err != nil {
		log.Fatalf("Error opening database: %v", err)
		return
	}
	defer db.Close()
	dbQueries := database.New(db)
	log.Printf("Database connected")

	cfg := &config.ApiConfig{
		Queries: dbQueries,
	}
	log.Printf("Config loaded")

	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterCarRentalServiceServer(s, &server{cfg: cfg})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
