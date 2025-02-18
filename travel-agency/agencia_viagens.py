from concurrent import futures
import grpc
import gRPC_pb2
import gRPC_pb2_grpc

'''
    API gRPC deve receber os seguintes parametros:
        tipo_passagem: int (1 (somente ida) ou 2 (ida e volta))
        data_ida: date
        data_volta: date
        origem: string
        destino: string
        numero_pessoas: int
'''

# Implementação do serviço definido no .proto
class AgenciaViagens(gRPC_pb2_grpc.AgenciaViagensServicer):
    def SolicitarPacoteViagem(self, request, context):
        print('Fazendo requisicao das passagens...')

        requisicao = gRPC_pb2.Requisicao(
                    data_ida=request.data_ida,
                    data_volta=request.data_volta,
                    origem=request.origem,
                    destino=request.destino,
                    numero_pessoas=request.numero_pessoas
                )

        SolicitarPacoteViagem(requisicao)

        # Criar o pacote de resposta
        resposta = gRPC_pb2.Resposta(
            sucesso=True,
            mensagem="sucesso"
        )

        return resposta

def SolicitarPassagens(gRPC_pb2.Requisicao requisicao):
    # Conecta no servidor gRPC
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = gRPC_pb2_grpc.CompaniaAereaStub(channel)

        response = stub.SolicitarPassagens(requisicao)
        print("Resposta do servidor:", response.mensagem)

        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gRPC_pb2_grpc.add_AgenciaViagensServicer_to_server(AgenciaViagens(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()