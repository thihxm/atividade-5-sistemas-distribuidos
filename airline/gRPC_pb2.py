# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gRPC.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'gRPC.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngRPC.proto\x12\x04gRPC\x1a\x1fgoogle/protobuf/timestamp.proto\"\xca\x01\n\nRequisicao\x12\x31\n\rcheck_in_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x0e\x63heck_out_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\x0e\n\x06origin\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x04 \x01(\t\x12\x18\n\x10number_of_people\x18\x05 \x01(\x05\x42\x11\n\x0f_check_out_date\"D\n\x08Resposta\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0ereservation_id\x18\x03 \x01(\t\"/\n\x15RequisicaoCompensacao\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t2K\n\x0e\x41genciaViagens\x12\x39\n\x15SolicitarPacoteViagem\x12\x10.gRPC.Requisicao\x1a\x0e.gRPC.Resposta2\x86\x01\n\rCompaniaAerea\x12\x36\n\x12SolicitarPassagens\x12\x10.gRPC.Requisicao\x1a\x0e.gRPC.Resposta\x12=\n\x0eReverterPedido\x12\x1b.gRPC.RequisicaoCompensacao\x1a\x0e.gRPC.Resposta2C\n\rRedeHoteleira\x12\x32\n\x0eSolicitarHotel\x12\x10.gRPC.Requisicao\x1a\x0e.gRPC.Resposta2@\n\x08Locadora\x12\x34\n\x10SolicitarVeiculo\x12\x10.gRPC.Requisicao\x1a\x0e.gRPC.Respostab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gRPC_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUISICAO']._serialized_start=54
  _globals['_REQUISICAO']._serialized_end=256
  _globals['_RESPOSTA']._serialized_start=258
  _globals['_RESPOSTA']._serialized_end=326
  _globals['_REQUISICAOCOMPENSACAO']._serialized_start=328
  _globals['_REQUISICAOCOMPENSACAO']._serialized_end=375
  _globals['_AGENCIAVIAGENS']._serialized_start=377
  _globals['_AGENCIAVIAGENS']._serialized_end=452
  _globals['_COMPANIAAEREA']._serialized_start=455
  _globals['_COMPANIAAEREA']._serialized_end=589
  _globals['_REDEHOTELEIRA']._serialized_start=591
  _globals['_REDEHOTELEIRA']._serialized_end=658
  _globals['_LOCADORA']._serialized_start=660
  _globals['_LOCADORA']._serialized_end=724
# @@protoc_insertion_point(module_scope)
