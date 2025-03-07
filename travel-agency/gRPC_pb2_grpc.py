# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import gRPC_pb2 as gRPC__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gRPC_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AgenciaViagensStub(object):
    """AgenciaViagens
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SolicitarPacoteViagem = channel.unary_unary(
                '/gRPC.AgenciaViagens/SolicitarPacoteViagem',
                request_serializer=gRPC__pb2.Requisicao.SerializeToString,
                response_deserializer=gRPC__pb2.Resposta.FromString,
                _registered_method=True)


class AgenciaViagensServicer(object):
    """AgenciaViagens
    """

    def SolicitarPacoteViagem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgenciaViagensServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SolicitarPacoteViagem': grpc.unary_unary_rpc_method_handler(
                    servicer.SolicitarPacoteViagem,
                    request_deserializer=gRPC__pb2.Requisicao.FromString,
                    response_serializer=gRPC__pb2.Resposta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gRPC.AgenciaViagens', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gRPC.AgenciaViagens', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AgenciaViagens(object):
    """AgenciaViagens
    """

    @staticmethod
    def SolicitarPacoteViagem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gRPC.AgenciaViagens/SolicitarPacoteViagem',
            gRPC__pb2.Requisicao.SerializeToString,
            gRPC__pb2.Resposta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class CompaniaAereaStub(object):
    """CompaniaAerea
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SolicitarPassagens = channel.unary_unary(
                '/gRPC.CompaniaAerea/SolicitarPassagens',
                request_serializer=gRPC__pb2.Requisicao.SerializeToString,
                response_deserializer=gRPC__pb2.Resposta.FromString,
                _registered_method=True)
        self.ReverterPedido = channel.unary_unary(
                '/gRPC.CompaniaAerea/ReverterPedido',
                request_serializer=gRPC__pb2.RequisicaoCompensacao.SerializeToString,
                response_deserializer=gRPC__pb2.Resposta.FromString,
                _registered_method=True)


class CompaniaAereaServicer(object):
    """CompaniaAerea
    """

    def SolicitarPassagens(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReverterPedido(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CompaniaAereaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SolicitarPassagens': grpc.unary_unary_rpc_method_handler(
                    servicer.SolicitarPassagens,
                    request_deserializer=gRPC__pb2.Requisicao.FromString,
                    response_serializer=gRPC__pb2.Resposta.SerializeToString,
            ),
            'ReverterPedido': grpc.unary_unary_rpc_method_handler(
                    servicer.ReverterPedido,
                    request_deserializer=gRPC__pb2.RequisicaoCompensacao.FromString,
                    response_serializer=gRPC__pb2.Resposta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gRPC.CompaniaAerea', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gRPC.CompaniaAerea', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CompaniaAerea(object):
    """CompaniaAerea
    """

    @staticmethod
    def SolicitarPassagens(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gRPC.CompaniaAerea/SolicitarPassagens',
            gRPC__pb2.Requisicao.SerializeToString,
            gRPC__pb2.Resposta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReverterPedido(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gRPC.CompaniaAerea/ReverterPedido',
            gRPC__pb2.RequisicaoCompensacao.SerializeToString,
            gRPC__pb2.Resposta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class RedeHoteleiraStub(object):
    """RedeHoteleira
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SolicitarHotel = channel.unary_unary(
                '/gRPC.RedeHoteleira/SolicitarHotel',
                request_serializer=gRPC__pb2.Requisicao.SerializeToString,
                response_deserializer=gRPC__pb2.Resposta.FromString,
                _registered_method=True)


class RedeHoteleiraServicer(object):
    """RedeHoteleira
    """

    def SolicitarHotel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedeHoteleiraServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SolicitarHotel': grpc.unary_unary_rpc_method_handler(
                    servicer.SolicitarHotel,
                    request_deserializer=gRPC__pb2.Requisicao.FromString,
                    response_serializer=gRPC__pb2.Resposta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gRPC.RedeHoteleira', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gRPC.RedeHoteleira', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RedeHoteleira(object):
    """RedeHoteleira
    """

    @staticmethod
    def SolicitarHotel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gRPC.RedeHoteleira/SolicitarHotel',
            gRPC__pb2.Requisicao.SerializeToString,
            gRPC__pb2.Resposta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class LocadoraStub(object):
    """Locadora
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SolicitarVeiculo = channel.unary_unary(
                '/gRPC.Locadora/SolicitarVeiculo',
                request_serializer=gRPC__pb2.Requisicao.SerializeToString,
                response_deserializer=gRPC__pb2.Resposta.FromString,
                _registered_method=True)


class LocadoraServicer(object):
    """Locadora
    """

    def SolicitarVeiculo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocadoraServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SolicitarVeiculo': grpc.unary_unary_rpc_method_handler(
                    servicer.SolicitarVeiculo,
                    request_deserializer=gRPC__pb2.Requisicao.FromString,
                    response_serializer=gRPC__pb2.Resposta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gRPC.Locadora', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gRPC.Locadora', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Locadora(object):
    """Locadora
    """

    @staticmethod
    def SolicitarVeiculo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gRPC.Locadora/SolicitarVeiculo',
            gRPC__pb2.Requisicao.SerializeToString,
            gRPC__pb2.Resposta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
