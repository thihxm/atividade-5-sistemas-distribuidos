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

class Passagem(object):
    def __init__(self, origem, destino, data, hora, estoque):
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora
        self.estoque = estoque

passagens_disponiveis = []

def preencher_passagens():
    passagem = Passagem('Curitiba', 'Sao Paulo', datetime(2025, 6, 25, 18, 0))

# Implementação do serviço definido no .proto
class CompaniaAerea(gRPC_pb2_grpc.CompaniaAereaServicer):
    def SolicitarPassagens(self, request, context):
        print('Processando pedido de passagens...')

        if request.data_volta is not None:
            

        # Criar o pacote de resposta
        resposta = gRPC_pb2.Resposta(
            sucesso=True,
            mensagem="sucesso"
        )

        return resposta

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gRPC_pb2_grpc.add_CompaniaAereaServicer_to_server(CompaniaAerea(), server)
    server.add_insecure_port('[::]:50052')
    print("Servidor gRPC rodando na porta 50052...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()