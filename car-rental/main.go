package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"
	"time"

	"github.com/google/uuid"
	base "github.com/thihxm/car-rental/proto/base"
	pb "github.com/thihxm/car-rental/proto/car-rental"
	"google.golang.org/grpc"
)

type Car struct {
	Brand string
	Model string
	Seats int32
	Price int32
}

type Reservation struct {
	Id        string
	Car       Car
	StartDate time.Time
	EndDate   time.Time
}

var (
	port          = flag.Int("port", 50051, "The server port")
	availableCars = []Car{}
	reservedCars  = []Reservation{}
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	pb.UnsafeCarRentalServiceServer
}

func findAvailableCar(requiredSeats int32) (*Car, error) {
	for _, car := range availableCars {
		if car.Seats >= requiredSeats {
			return &car, nil
		}
	}
	return nil, fmt.Errorf("no available car found with %d or more seats", requiredSeats)
}

func findReservedCar(reservationId string) (*Reservation, error) {
	for _, reservation := range reservedCars {
		if reservation.Id == reservationId {
			return &reservation, nil
		}
	}
	return nil, fmt.Errorf("no reserved car found with id %s", reservationId)
}

func removeCar(cars []Car, car Car) []Car {
	for i, c := range cars {
		if c == car {
			return append(cars[:i], cars[i+1:]...)
		}
	}
	return cars
}

func removeReservation(reservations []Reservation, reservation Reservation) []Reservation {
	for i, r := range reservations {
		if r.Id == reservation.Id {
			return append(reservations[:i], reservations[i+1:]...)
		}
	}
	return reservations
}

func (s *server) RentCar(_ context.Context, in *base.CreateReservationRequest) (*base.CreateReservationResponse, error) {
	log.Printf("Received: %v", in.GetCheckInDate())
	var success = true
	var message = "Car rented successfully"

	car, err := findAvailableCar(in.GetNumberOfPeople())
	if err != nil {
		success = false
		message = err.Error()

		var responseBuilder = base.CreateReservationResponse_builder{
			Success: &success,
			Message: &message,
		}
		return responseBuilder.Build(), nil
	}

	availableCars = removeCar(availableCars, *car)

	var reservation = Reservation{
		Id:  uuid.New().String(),
		Car: *car,
	}

	reservedCars = append(reservedCars, reservation)

	var responseBuilder = base.CreateReservationResponse_builder{
		Success:       &success,
		Message:       &message,
		ReservationId: &reservation.Id,
	}
	return responseBuilder.Build(), nil
}

func (s *server) RevertBooking(_ context.Context, in *base.RevertBookingRequest) (*base.RevertBookingResponse, error) {
	log.Printf("Received: %v", in.GetReservationId())
	var success = true
	var message = "Car returned successfully"

	reservedCar, err := findReservedCar(in.GetReservationId())
	if err != nil {
		success = false
		message = err.Error()
	} else {
		availableCars = append(availableCars, reservedCar.Car)
		reservedCars = removeReservation(reservedCars, *reservedCar)
	}

	var responseBuilder = base.RevertBookingResponse_builder{
		Success: &success,
		Message: &message,
	}
	return responseBuilder.Build(), nil
}

func main() {
	availableCars = []Car{
		{Brand: "Chevrolet", Model: "Onix", Seats: 5, Price: 100000},
		{Brand: "Volkswagen", Model: "Up", Seats: 4, Price: 200000},
		{Brand: "Fiat", Model: "Palio", Seats: 5, Price: 200000},
	}

	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterCarRentalServiceServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
