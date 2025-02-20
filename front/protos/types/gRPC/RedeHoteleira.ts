// Original file: protos/proto/gRPC.proto

import type * as grpc from '@grpc/grpc-js'
import type { MethodDefinition } from '@grpc/proto-loader'
import type { Requisicao as _gRPC_Requisicao, Requisicao__Output as _gRPC_Requisicao__Output } from '../gRPC/Requisicao';
import type { Resposta as _gRPC_Resposta, Resposta__Output as _gRPC_Resposta__Output } from '../gRPC/Resposta';

/**
 * RedeHoteleira
 */
export interface RedeHoteleiraClient extends grpc.Client {
  SolicitarHotel(argument: _gRPC_Requisicao, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  SolicitarHotel(argument: _gRPC_Requisicao, metadata: grpc.Metadata, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  SolicitarHotel(argument: _gRPC_Requisicao, options: grpc.CallOptions, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  SolicitarHotel(argument: _gRPC_Requisicao, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  solicitarHotel(argument: _gRPC_Requisicao, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  solicitarHotel(argument: _gRPC_Requisicao, metadata: grpc.Metadata, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  solicitarHotel(argument: _gRPC_Requisicao, options: grpc.CallOptions, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  solicitarHotel(argument: _gRPC_Requisicao, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  
}

/**
 * RedeHoteleira
 */
export interface RedeHoteleiraHandlers extends grpc.UntypedServiceImplementation {
  SolicitarHotel: grpc.handleUnaryCall<_gRPC_Requisicao__Output, _gRPC_Resposta>;
  
}

export interface RedeHoteleiraDefinition extends grpc.ServiceDefinition {
  SolicitarHotel: MethodDefinition<_gRPC_Requisicao, _gRPC_Resposta, _gRPC_Requisicao__Output, _gRPC_Resposta__Output>
}
