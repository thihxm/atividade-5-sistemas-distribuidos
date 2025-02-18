import * as grpc from "@grpc/grpc-js";
import * as protoLoader from "@grpc/proto-loader";
import { ProtoGrpcType } from "./types/reservations";
const PORT = 8082;
const RESERVATIONS_PROTO_FILE = "reservations.proto";
const packageDef = protoLoader.loadSync(RESERVATIONS_PROTO_FILE, {
    keepCase: false,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
    includeDirs: ["./protos/proto"],
});
const grpcObj = grpc.loadPackageDefinition(
    packageDef
) as unknown as ProtoGrpcType;

export default function createReservationsClient() {
    return new grpcObj.reservations.Reservations(
        `0.0.0.0:${PORT}`,
        grpc.credentials.createInsecure()
    );
}
