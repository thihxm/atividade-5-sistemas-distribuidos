-- +goose Up
CREATE TABLE reservations (
    id TEXT PRIMARY KEY,
    car_id TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (car_id) REFERENCES cars(id)
);

-- +goose Down
DROP TABLE reservations;