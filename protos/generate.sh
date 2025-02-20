#!/bin/bash
# Let's call this script venv.sh
echo "Activating venv"
source "$(dirname "$0")/../.venv/bin/activate"

echo "Generating car-rental"
python -m grpc_tools.protoc --proto_path="$(dirname "$0")" --go_out="$(dirname "$0")"/../car-rental/protos/car-rental --go_opt=Mbase.proto=github.com/thihxm/car-rental/protos/base --go_opt=paths=source_relative --go-grpc_out="$(dirname "$0")"/../car-rental/protos/car-rental --go-grpc_opt=Mbase.proto=github.com/thihxm/car-rental/protos/base --go-grpc_opt=paths=source_relative --go_opt=default_api_level=API_OPAQUE --python_out="$(dirname "$0")"/../travel-agency/protos/car-rental --grpc_python_out="$(dirname "$0")"/../travel-agency/protos/car-rental car-rental.proto

echo "Generating hotel-chain"
python -m grpc_tools.protoc --proto_path="$(dirname "$0")" --go_out="$(dirname "$0")"/../hotel-chain/protos/hotel-chain --go_opt=Mbase.proto=github.com/thihxm/hotel-chain/protos/base --go_opt=paths=source_relative --go-grpc_out="$(dirname "$0")"/../hotel-chain/protos/hotel-chain --go-grpc_opt=Mbase.proto=github.com/thihxm/hotel-chain/protos/base --go-grpc_opt=paths=source_relative --go_opt=default_api_level=API_OPAQUE --python_out="$(dirname "$0")"/../travel-agency/protos/hotel-chain --grpc_python_out="$(dirname "$0")"/../travel-agency/protos/hotel-chain hotel-chain.proto

echo "Generating base"
python -m grpc_tools.protoc --proto_path="$(dirname "$0")" --python_out="$(dirname "$0")"/../travel-agency/protos/base --grpc_python_out="$(dirname "$0")"/../travel-agency/protos/base base.proto