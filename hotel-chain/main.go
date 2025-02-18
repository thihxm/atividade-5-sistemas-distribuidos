package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"
	"strings"
	"time"

	"github.com/google/uuid"
	base "github.com/thihxm/hotel-chain/proto/base"
	pb "github.com/thihxm/hotel-chain/proto/hotel-chain"
	"google.golang.org/grpc"
)

type Room struct {
	Id        string
	Name      string
	Location  string
	MaxPeople int32
	Price     int32
}

type Reservation struct {
	Id        string
	Room      Room
	StartDate time.Time
	EndDate   *time.Time
}

var (
	port           = flag.Int("port", 50051, "The server port")
	availableRooms = []Room{}
	reservedRooms  = []Reservation{}
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	pb.UnimplementedHotelServiceServer
}

func findAvailableRoom(requiredPeople int32, location string, checkInDate time.Time, checkOutDate *time.Time) (*Room, error) {
	for _, room := range availableRooms {
		if room.MaxPeople >= requiredPeople && strings.ToLower(room.Location) == strings.ToLower(location) {
			isAvailable := true
			for _, reservation := range reservedRooms {
				if reservation.Room.Id == room.Id {
					// Case 1: Existing reservation has no end date (ongoing)
					if reservation.EndDate == nil {
						if !checkInDate.Before(reservation.StartDate) {
							isAvailable = false
							break
						}
					} else {
						// Case 2: New reservation has no checkout date (ongoing)
						if checkOutDate == nil {
							if !checkInDate.After(*reservation.EndDate) {
								isAvailable = false
								break
							}
						} else {
							// Case 3: Both reservations have start/end dates
							// Check if there's any overlap in the date ranges
							if !(checkInDate.After(*reservation.EndDate) || checkOutDate.Before(reservation.StartDate)) {
								isAvailable = false
								break
							}
						}
					}
				}
			}
			if isAvailable {
				return &room, nil
			}
		}
	}
	return nil, fmt.Errorf("no available room found with %d or more people at %s", requiredPeople, location)
}

func findReservedRoom(reservationId string) (*Reservation, error) {
	for _, reservation := range reservedRooms {
		if reservation.Id == reservationId {
			return &reservation, nil
		}
	}
	return nil, fmt.Errorf("no reserved room found with id %s", reservationId)
}

func removeReservation(reservations []Reservation, reservation Reservation) []Reservation {
	for i, r := range reservations {
		if r.Id == reservation.Id {
			return append(reservations[:i], reservations[i+1:]...)
		}
	}
	return reservations
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
	room, err := findAvailableRoom(in.GetNumberOfPeople(), in.GetDestination(), in.GetCheckInDate().AsTime(), checkOutDate)
	if err != nil {
		success = false
		message = err.Error()
		var responseBuilder = base.CreateReservationResponse_builder{
			Success: success,
			Message: message,
		}
		return responseBuilder.Build(), nil
	}

	var reservation = Reservation{
		Id:   uuid.New().String(),
		Room: *room,
	}
	reservedRooms = append(reservedRooms, reservation)

	var responseBuilder = base.CreateReservationResponse_builder{
		Success:       success,
		Message:       message,
		ReservationId: reservation.Id,
	}

	return responseBuilder.Build(), nil
}

func (s *server) RevertBooking(_ context.Context, in *base.RevertBookingRequest) (*base.RevertBookingResponse, error) {
	log.Printf("Received: %v", in.GetReservationId())
	var success = true
	var message = "Hotel reservation reverted successfully"

	reservedRoom, err := findReservedRoom(in.GetReservationId())
	if err != nil {
		success = false
		message = err.Error()
	} else {
		reservedRooms = removeReservation(reservedRooms, *reservedRoom)
	}

	var responseBuilder = base.RevertBookingResponse_builder{
		Success: success,
		Message: message,
	}
	return responseBuilder.Build(), nil
}

func main() {
	availableRooms = []Room{
		{Id: "1", Name: "Quarto SP", Location: "São Paulo", MaxPeople: 2, Price: 100},
		{Id: "2", Name: "Quarto CWB", Location: "Curitiba", MaxPeople: 4, Price: 200},
		{Id: "3", Name: "Quarto RIO", Location: "Rio de Janeiro", MaxPeople: 3, Price: 300},
	}

	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterHotelServiceServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
