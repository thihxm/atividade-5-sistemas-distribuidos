// Original file: protos/proto/gRPC.proto

import type * as grpc from '@grpc/grpc-js'
import type { MethodDefinition } from '@grpc/proto-loader'
import type { Requisicao as _gRPC_Requisicao, Requisicao__Output as _gRPC_Requisicao__Output } from '../gRPC/Requisicao';
import type { Resposta as _gRPC_Resposta, Resposta__Output as _gRPC_Resposta__Output } from '../gRPC/Resposta';

/**
 * CompaniaAerea
 */
export interface CompaniaAereaClient extends grpc.Client {
  SolicitarPassagens(argument: _gRPC_Requisicao, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  SolicitarPassagens(argument: _gRPC_Requisicao, metadata: grpc.Metadata, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  SolicitarPassagens(argument: _gRPC_Requisicao, options: grpc.CallOptions, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  SolicitarPassagens(argument: _gRPC_Requisicao, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  solicitarPassagens(argument: _gRPC_Requisicao, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  solicitarPassagens(argument: _gRPC_Requisicao, metadata: grpc.Metadata, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  solicitarPassagens(argument: _gRPC_Requisicao, options: grpc.CallOptions, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  solicitarPassagens(argument: _gRPC_Requisicao, callback: grpc.requestCallback<_gRPC_Resposta__Output>): grpc.ClientUnaryCall;
  
}

/**
 * CompaniaAerea
 */
export interface CompaniaAereaHandlers extends grpc.UntypedServiceImplementation {
  SolicitarPassagens: grpc.handleUnaryCall<_gRPC_Requisicao__Output, _gRPC_Resposta>;
  
}

export interface CompaniaAereaDefinition extends grpc.ServiceDefinition {
  SolicitarPassagens: MethodDefinition<_gRPC_Requisicao, _gRPC_Resposta, _gRPC_Requisicao__Output, _gRPC_Resposta__Output>
}
