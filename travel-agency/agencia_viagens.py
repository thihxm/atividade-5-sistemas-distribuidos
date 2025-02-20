import os  # noqa
import sys  # noqa
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'protos/base'))  # noqa
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), 'protos/car-rental'))  # noqa
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), 'protos/hotel-chain'))  # noqa

import grpc
import gRPC_pb2
import gRPC_pb2_grpc
import base_pb2
import car_rental_pb2_grpc
import hotel_chain_pb2_grpc
from concurrent import futures


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

        if request.HasField("check_out_date"):
            createReservationRequest = base_pb2.CreateReservationRequest(
                check_in_date=request.check_in_date,
                check_out_date=request.check_out_date,
                origin=request.origin,
                destination=request.destination,
                number_of_people=request.number_of_people
            )
        else:
            createReservationRequest = base_pb2.CreateReservationRequest(
                check_in_date=request.check_in_date,
                origin=request.origin,
                destination=request.destination,
                number_of_people=request.number_of_people
            )

        # resposta = SolicitarPassagens(requisicao)

        # Conecta no servidor gRPC
        with grpc.insecure_channel('localhost:50052') as channel, grpc.insecure_channel('localhost:50053') as channel_hotel, grpc.insecure_channel('localhost:50054') as channel_car:
            # with grpc.insecure_channel('localhost:50053') as channel_hotel, grpc.insecure_channel('localhost:50054') as channel_car:

            stub = gRPC_pb2_grpc.CompaniaAereaStub(channel)
            stub_hotel = hotel_chain_pb2_grpc.HotelServiceStub(
                channel_hotel)
            stub_car = car_rental_pb2_grpc.CarRentalServiceStub(
                channel_car)

            response = stub.SolicitarPassagens(requisicao)
            print("Resposta do servidor:", response.message)

            if not response.success:
                response = gRPC_pb2.Resposta(
                    success=response.success,
                    message=response.message
                )

                return response

            response_hotel = stub_hotel.BookHotel(createReservationRequest)
            print("Resposta do Hotel:", response_hotel.message)

            if not response_hotel.success:
                response_hotel = gRPC_pb2.Resposta(
                    success=response_hotel.success,
                    message=response_hotel.message
                )
                # return response_hotel
                requisicao_compensacao = gRPC_pb2.RequisicaoCompensacao(
                    reservation_id=response.reservation_id
                )

                response = stub.ReverterPedido(requisicao_compensacao)
                print("Resposta do Reverter Passagens:", response.message)
                
                return response_hotel

            response_car = stub_car.RentCar(createReservationRequest)
            print("Resposta do Aluguel de Carros:", response_car.message)

            if not response_car.success:
                requisicao_compensacao = gRPC_pb2.RequisicaoCompensacao(
                    reservation_id=response.reservation_id
                )

                response = stub.ReverterPedido(requisicao_compensacao)
                print("Resposta do Reverter Pedido de Passagens:", response.message)
                response = stub_hotel.RevertBooking(requisicao_compensacao)
                print("Resposta do Reverter Pedido do Hotel:", response.message)
                response = gRPC_pb2.Resposta(
                    success=response.success,
                    message=response.message
                )
                return response_car

            response = gRPC_pb2.Resposta(
                success=True,
                message="Pacote de viagem completo solicitado com sucesso!"
            )
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

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gRPC_pb2_grpc.add_AgenciaViagensServicer_to_server(
        AgenciaViagens(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC rodando na porta 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()