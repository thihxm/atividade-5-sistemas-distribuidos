package config

import (
	"github.com/thihxm/hotel-chain/internal/database"
)

type ApiConfig struct {
	Queries *database.Queries
}
