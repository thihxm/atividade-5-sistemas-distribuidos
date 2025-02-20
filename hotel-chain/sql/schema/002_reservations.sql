-- +goose Up
CREATE TABLE reservations (
    id TEXT PRIMARY KEY,
    room_id TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

-- +goose Down
DROP TABLE reservations;