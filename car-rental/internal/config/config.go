package config

import (
	"github.com/thihxm/car-rental/internal/database"
)

type ApiConfig struct {
	Queries *database.Queries
}
