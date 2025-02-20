-- +goose Up
CREATE TABLE cars (
    id TEXT PRIMARY KEY,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    seats INT NOT NULL,
    price INT NOT NULL,
    location TEXT NOT NULL
);

-- +goose Down
DROP TABLE cars;