-- name: GetFirstAvailableCar :one
SELECT * FROM cars
WHERE location = ? 
AND seats >= ? 
AND id NOT IN (
    SELECT car_id FROM reservations
    WHERE start_date <= ? AND end_date >= ?
)
LIMIT 1;

-- name: CreateCar :exec
INSERT INTO cars (id, brand, model, seats, price, location)
VALUES (?, ?, ?, ?, ?, ?);
