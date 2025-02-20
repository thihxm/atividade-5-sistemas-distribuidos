import type * as grpc from '@grpc/grpc-js';
import type { MessageTypeDefinition } from '@grpc/proto-loader';

import type { AgenciaViagensClient as _gRPC_AgenciaViagensClient, AgenciaViagensDefinition as _gRPC_AgenciaViagensDefinition } from './gRPC/AgenciaViagens';
import type { CompaniaAereaClient as _gRPC_CompaniaAereaClient, CompaniaAereaDefinition as _gRPC_CompaniaAereaDefinition } from './gRPC/CompaniaAerea';
import type { LocadoraClient as _gRPC_LocadoraClient, LocadoraDefinition as _gRPC_LocadoraDefinition } from './gRPC/Locadora';
import type { RedeHoteleiraClient as _gRPC_RedeHoteleiraClient, RedeHoteleiraDefinition as _gRPC_RedeHoteleiraDefinition } from './gRPC/RedeHoteleira';

type SubtypeConstructor<Constructor extends new (...args: any) => any, Subtype> = {
  new(...args: ConstructorParameters<Constructor>): Subtype;
};

export interface ProtoGrpcType {
  gRPC: {
    /**
     * AgenciaViagens
     */
    AgenciaViagens: SubtypeConstructor<typeof grpc.Client, _gRPC_AgenciaViagensClient> & { service: _gRPC_AgenciaViagensDefinition }
    /**
     * CompaniaAerea
     */
    CompaniaAerea: SubtypeConstructor<typeof grpc.Client, _gRPC_CompaniaAereaClient> & { service: _gRPC_CompaniaAereaDefinition }
    /**
     * Locadora
     */
    Locadora: SubtypeConstructor<typeof grpc.Client, _gRPC_LocadoraClient> & { service: _gRPC_LocadoraDefinition }
    /**
     * RedeHoteleira
     */
    RedeHoteleira: SubtypeConstructor<typeof grpc.Client, _gRPC_RedeHoteleiraClient> & { service: _gRPC_RedeHoteleiraDefinition }
    Requisicao: MessageTypeDefinition
    RequisicaoCompensacao: MessageTypeDefinition
    Resposta: MessageTypeDefinition
  }
  google: {
    protobuf: {
      Timestamp: MessageTypeDefinition
    }
  }
}

