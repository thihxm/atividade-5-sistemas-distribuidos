// Cars Seeding

package main

import (
	"context"
	"database/sql"
	"log"

	"github.com/google/uuid"
	"github.com/thihxm/car-rental/internal/database"
)

func main() {
	db, err := sql.Open("sqlite3", "./car-rental.db")
	if err != nil {
		log.Fatalf("Error opening database: %v", err)
	}
	defer db.Close()

	queries := database.New(db)

	queries.CreateCar(context.Background(), database.CreateCarParams{
		ID:       uuid.New().String(),
		Brand:    "Chevrolet",
		Model:    "Onix",
		Seats:    5,
		Price:    100000,
		Location: "Sao Paulo",
	})

	queries.CreateCar(context.Background(), database.CreateCarParams{
		ID:       uuid.New().String(),
		Brand:    "Volkswagen",
		Model:    "Up",
		Seats:    4,
		Price:    200000,
		Location: "Sao Paulo",
	})

	queries.CreateCar(context.Background(), database.CreateCarParams{
		ID:       uuid.New().String(),
		Brand:    "Fiat",
		Model:    "Palio",
		Seats:    5,
		Price:    200000,
		Location: "Rio de Janeiro",
	})
}
