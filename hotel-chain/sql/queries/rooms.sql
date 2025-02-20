-- name: GetFirstAvailableRoom :one
SELECT * FROM rooms
WHERE location = ? 
AND max_people >= ? 
AND id NOT IN (
    SELECT room_id FROM reservations
    WHERE start_date <= ? AND end_date >= ?
)
LIMIT 1;

-- name: CreateRoom :exec
INSERT INTO rooms (id, name, location, max_people, price)
VALUES (?, ?, ?, ?, ?);

-- name: ResetRooms :exec
DELETE FROM rooms;
