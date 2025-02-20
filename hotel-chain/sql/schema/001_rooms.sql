-- +goose Up
CREATE TABLE rooms (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    max_people INT NOT NULL,
    price INT NOT NULL
);

-- +goose Down
DROP TABLE rooms;