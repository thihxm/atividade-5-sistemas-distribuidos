// Cars Seeding

package main

import (
	"context"
	"database/sql"
	"log"

	"github.com/google/uuid"
	"github.com/thihxm/hotel-chain/internal/database"
)

func main() {
	db, err := sql.Open("sqlite3", "./hotel-chain.db")
	if err != nil {
		log.Fatalf("Error opening database: %v", err)
	}
	defer db.Close()

	queries := database.New(db)

	queries.ResetRooms(context.Background())
	queries.ResetReservations(context.Background())

	queries.CreateRoom(context.Background(), database.CreateRoomParams{
		ID:        uuid.New().String(),
		Name:      "Quarto SP",
		Location:  "Sao Paulo",
		MaxPeople: 2,
		Price:     10000,
	})

	queries.CreateRoom(context.Background(), database.CreateRoomParams{
		ID:        uuid.New().String(),
		Name:      "Quarto CWB",
		Location:  "Curitiba",
		MaxPeople: 4,
		Price:     20000,
	})

	queries.CreateRoom(context.Background(), database.CreateRoomParams{
		ID:        uuid.New().String(),
		Name:      "Quarto RIO",
		Location:  "Rio de Janeiro",
		MaxPeople: 3,
		Price:     30000,
	})
}
