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

        if request.HasField("check_out_date"):
            requisicao = gRPC_pb2.Requisicao(
                        check_in_date=request.check_in_date,
                        check_out_date=request.check_out_date,
                        origin=request.origin,
                        destination=request.destination,
                        number_of_people=request.number_of_people
                    )
        else:
            requisicao = gRPC_pb2.Requisicao(
                        check_in_date=request.check_in_date,
                        origin=request.origin,
                        destination=request.destination,
                        number_of_people=request.number_of_people
                    )

        #resposta = SolicitarPassagens(requisicao)

        # Conecta no servidor gRPC
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = gRPC_pb2_grpc.CompaniaAereaStub(channel)

            response = stub.SolicitarPassagens(requisicao)
            print("Resposta do servidor:", response.message)

            # testando a compensacao
            '''if(response.success):
                requisicao_compensacao = gRPC_pb2.RequisicaoCompensacao(
                    reservation_id = response.reservation_id
                )
            
                response = stub.ReverterPedido(requisicao_compensacao)
            '''
            return response

'''
        with grpc.insecure_channel('localhost:50052') as channel_a, \
            grpc.insecure_channel('localhost:50053') as channel_b, \
            grpc.insecure_channel('localhost:50054') as channel_c:
            
            # Criar os stubs para os serviços gRPC
            stub_a = gRPC_pb2_grpc.CompaniaAereaStub(channel_a)
            stub_b = gRPC_pb2_grpc.HotelStub(channel_b)
            stub_c = gRPC_pb2_grpc.AluguelCarrosStub(channel_c)

            # Fazer a requisição para a companhia aérea
            response_a = stub_a.SolicitarPassagens(requisicao)
            print("Resposta da Companhia Aérea:", response_a.message)

            # Fazer a requisição para o serviço de hotel
            response_b = stub_b.ReservarHotel(requisicao)
            print("Resposta do Hotel:", response_b.message)

            # Fazer a requisição para o serviço de aluguel de carros
            response_c = stub_c.ReservarCarro(requisicao)
            print("Resposta do Aluguel de Carros:", response_c.message)

            return response_a, response_b, response_c  # Retorna as respostas dos três serviços
'''


        # Criar o pacote de resposta
        #resposta = gRPC_pb2.Resposta(
        #    sucesso=True,
        #    mensagem="sucesso"
        #)
'''
def SolicitarPassagens(gRPC_pb2.Requisicao requisicao):
    # Conecta no servidor gRPC
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = gRPC_pb2_grpc.CompaniaAereaStub(channel)

        response = stub.SolicitarPassagens(requisicao)
        print("Resposta do servidor:", response.mensagem)

        return response
'''

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gRPC_pb2_grpc.add_AgenciaViagensServicer_to_server(AgenciaViagens(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()