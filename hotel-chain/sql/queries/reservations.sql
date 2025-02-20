-- name: CreateReservation :one
INSERT INTO reservations (id, room_id, start_date, end_date)
VALUES (?, ?, ?, ?)
RETURNING *;

-- name: GetReservation :one
SELECT * FROM reservations
WHERE id = ?;

-- name: DeleteReservation :exec
DELETE FROM reservations
WHERE id = ?;

-- name: ResetReservations :exec
DELETE FROM reservations;