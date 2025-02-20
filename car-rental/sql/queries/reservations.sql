-- name: CreateReservation :one
INSERT INTO reservations (id, car_id, start_date, end_date)
VALUES (?, ?, ?, ?)
RETURNING *;