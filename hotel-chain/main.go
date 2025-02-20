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
	"github.com/thihxm/hotel-chain/internal/config"
	"github.com/thihxm/hotel-chain/internal/database"
	base "github.com/thihxm/hotel-chain/protos/base"
	pb "github.com/thihxm/hotel-chain/protos/hotel-chain"
	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 50053, "The server port")
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	pb.UnimplementedHotelServiceServer
	cfg *config.ApiConfig
}

func findAvailableRoom(cfg *config.ApiConfig, requiredPeople int32, location string, checkInDate time.Time, checkOutDate *time.Time) (*database.Room, error) {
	room, err := cfg.Queries.GetFirstAvailableRoom(context.Background(), database.GetFirstAvailableRoomParams{
		Location:  location,
		MaxPeople: int64(requiredPeople),
		StartDate: checkInDate,
		EndDate:   sql.NullTime{Time: *checkOutDate, Valid: checkOutDate != nil},
	})
	if err != nil {
		return nil, err
	}
	return &room, nil
}

func findReservedRoom(cfg *config.ApiConfig, reservationId string) (*database.Reservation, error) {
	reservation, err := cfg.Queries.GetReservation(context.Background(), reservationId)
	if err != nil {
		return nil, err
	}
	return &reservation, nil
}

func (s *server) BookHotel(_ context.Context, in *base.CreateReservationRequest) (*base.CreateReservationResponse, error) {
	log.Printf("Received: %v", in.GetCheckInDate())
	var success = true
	var message = "Hotel booked successfully"

	var checkOutDate *time.Time
	if in.GetCheckOutDate() != nil {
		parsedCheckOutDate := in.GetCheckOutDate().AsTime()
		checkOutDate = &parsedCheckOutDate
	}
	room, err := findAvailableRoom(s.cfg, in.GetNumberOfPeople(), in.GetDestination(), in.GetCheckInDate().AsTime(), checkOutDate)
	if err != nil {
		success = false
		message = err.Error()
		var responseBuilder = base.CreateReservationResponse_builder{
			Success: success,
			Message: message,
		}
		return responseBuilder.Build(), nil
	}

	reservation, err := s.cfg.Queries.CreateReservation(context.Background(), database.CreateReservationParams{
		ID:        uuid.New().String(),
		RoomID:    room.ID,
		StartDate: in.GetCheckInDate().AsTime(),
		EndDate:   sql.NullTime{Time: *checkOutDate, Valid: checkOutDate != nil},
	})
	if err != nil {
		success = false
		message = err.Error()
	}

	var responseBuilder = base.CreateReservationResponse_builder{
		Success:       success,
		Message:       message,
		ReservationId: &reservation.ID,
	}

	return responseBuilder.Build(), nil
}

func (s *server) RevertBooking(_ context.Context, in *base.RevertBookingRequest) (*base.RevertBookingResponse, error) {
	log.Printf("Received: %v", in.GetReservationId())
	var success = true
	var message = "Hotel reservation reverted successfully"

	reservedRoom, err := findReservedRoom(s.cfg, in.GetReservationId())
	if err != nil {
		success = false
		message = err.Error()
	} else {
		err = s.cfg.Queries.DeleteReservation(context.Background(), reservedRoom.ID)
		if err != nil {
			success = false
			message = err.Error()
		}
	}

	var responseBuilder = base.RevertBookingResponse_builder{
		Success: success,
		Message: message,
	}
	return responseBuilder.Build(), nil
}

func main() {
	db, err := sql.Open("sqlite3", "./hotel-chain.db")
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
	pb.RegisterHotelServiceServer(s, &server{cfg: cfg})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
