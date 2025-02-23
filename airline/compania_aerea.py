from concurrent import futures
import grpc
import gRPC_pb2
import gRPC_pb2_grpc
import uuid
import sqlite3
from google.protobuf.timestamp_pb2 import Timestamp

'''
    API gRPC deve receber os seguintes parametros:
        --tipo_passagem: int (1 (somente ida) ou 2 (ida e volta))
        data_ida: date
        optional data_volta: date
        origem: string
        destino: string
        numero_pessoas: int
'''

pedidos_realizados = []

pedidos_revertidos = []

# Encontrar passagem no banco ao realizar pedido
def buscar_passagens(origem, destino, data, numero_pessoas):
    nome_arquivo_banco = "airline_db.db"
    conexao = sqlite3.connect(nome_arquivo_banco)
    cursor = conexao.cursor()

    # Converter a data para string no formato ISO
    data_str = data.strftime('%Y-%m-%d %H:%M:%S')

    #print(f'data: {data_str}')

    cursor.execute('''SELECT id, estoque
                      FROM passagem 
                      WHERE origem = ? AND destino = ? and data = ?''', (origem, destino, data_str))

    passagem = cursor.fetchall()

    conexao.close()

    #print(f'data2: {data_str}')

    if not passagem: 
        return None

    # Caso o numero de passagens seja insuficiente
    if passagem[0][1] < numero_pessoas:
        return None
    
    return passagem

# Incrementa ou decrementa o estoque de uma passagem no banco


def atualizar_estoque(id_passagem, n):
    nome_arquivo_banco = "airline_db.db"
    conexao = sqlite3.connect(nome_arquivo_banco)
    cursor = conexao.cursor()

    if (n > 0):
        cursor.execute('''UPDATE passagem
                        SET estoque = estoque + ? 
                        WHERE id = ?''', (n, id_passagem))
    else:
        n = n * (-1)
        cursor.execute('''UPDATE passagem
                        SET estoque = estoque - ? 
                        WHERE id = ?''', (n, id_passagem))

    conexao.commit()

    cursor.execute(
        "SELECT id, origem, destino, estoque FROM passagem WHERE id = ?", (id_passagem, ))
    passagem = cursor.fetchall()

    print('Atualizacao de Estoque:')
    for item in passagem:
        print(f"    ID passagem: {item[0]}")
        print(f"    origem: {item[1]}")
        print(f"    destino: {item[2]}")
        print(f"    estoque atual: {item[3]}")
        print("    " + "-" * 20)

    cursor.close()
    conexao.close()

    return

# Busca pedidos não cancelados no banco e insere-os na lista pedidos_realizados


def buscar_pedidos():
    conn = sqlite3.connect("airline_db.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, id_passagem_ida, id_passagem_volta, numero_pessoas, mensagem, cancelado FROM pedido WHERE cancelado = 0")
    pedidos = cursor.fetchall()

    for pedido in pedidos:
        pedido_dict = {
            "id": pedido[0],
            "id_passagem_ida": pedido[1],
            "id_passagem_volta": pedido[2] if pedido[2] is not None else 0,
            "numero_pessoas": pedido[3],
            "mensagem": pedido[4] if pedido[4] else "Passagem reservada com sucesso",
            "cancelado": pedido[5]
        }
        pedidos_realizados.append(pedido_dict)

    # Fechar conexão com o banco
    conn.close()

    return

# Cancelar pedido no banco


def cancelar_pedido(id_pedido):
    print(f'Excluindo pedido {id_pedido} no banco...')

    conn = sqlite3.connect("airline_db.db")
    cursor = conn.cursor()

    cursor.execute(''' 
                    UPDATE pedido
                    SET cancelado = 1
                    WHERE id = ?
                    ''', (id_pedido, ))

    conn.commit()

    # Fechar conexão com o banco
    conn.close()

    return

# Salva pedido no banco


def salvar_pedido(pedido):
    print(f'Salvando pedido {pedido["id"]} no banco...')

    nome_arquivo_banco = "airline_db.db"
    conexao = sqlite3.connect(nome_arquivo_banco)
    cursor = conexao.cursor()

    cursor.execute("""
                INSERT INTO pedido (id, id_passagem_ida, id_passagem_volta, numero_pessoas, mensagem, cancelado)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (pedido["id"], pedido["id_passagem_ida"], pedido["id_passagem_volta"], pedido["numero_pessoas"], pedido["mensagem"], pedido["cancelado"]))

    conexao.commit()

    cursor.execute(
        "SELECT id, id_passagem_ida, id_passagem_volta, numero_pessoas, mensagem, cancelado FROM pedido")
    pedidos = cursor.fetchall()
    '''
    print('Pedidos no Banco:')
    for item in pedidos:
        print(f"    ID pedido: {item[0]}")
        print(f"    ID passagem ida: {item[1]}")
        print(f"    ID passagem volta: {item[2]}")
        print(f"    Numero de pessoas: {item[3]}")
        print("    " + "-" * 20)
    '''
    cursor.close()
    conexao.close()

    return

# Busca passagem e atualiza o estoque - Somente ida


def pedido_somente_ida(dados):

    check_in_date = dados.check_in_date.ToDatetime()
    passagem = buscar_passagens(dados.origin, dados.destination, check_in_date, dados.number_of_people)

    if passagem is None:
        pedido = {
            "id": 0,
            "mensagem": "Error - tickets unavailable"
        }
        return pedido
    else:
        atualizar_estoque(passagem[0][0], dados.number_of_people * (-1))
        #print(f'ID Passagem ida: {passagem[0][0]}')
        pedido = {
            "id": str(uuid.uuid4()),
            "id_passagem_ida": passagem[0][0],
            "id_passagem_volta": 0,
            "numero_pessoas": dados.number_of_people,
            "mensagem": "Passagem reservada com sucesso",
            "cancelado": 0
        }
        salvar_pedido(pedido)
        pedidos_realizados.append(pedido)
        return pedido

# Busca passagem e atualiza o estoque - Ida e volta


def pedido_ida_volta(dados):
    #print('metodo pedido')
    
    check_in_date = dados.check_in_date.ToDatetime()  # Converte Timestamp para datetime
    check_out_date = dados.check_out_date.ToDatetime()  # Converte Timestamp para datetime

    #print(f'dados: {dados.origin, dados.destination, check_in_date, check_out_date}')

    passagem_ida = buscar_passagens(dados.origin, dados.destination, check_in_date, dados.number_of_people)
    passagem_volta = buscar_passagens(dados.destination, dados.origin, check_out_date, dados.number_of_people)
    #print('passagem buscada')
    if passagem_ida is None or passagem_volta is None:
        pedido = {
            "id": 0,
            "mensagem": "Error - tickets unavailable"
        }
        return pedido
    else:
        atualizar_estoque(passagem_ida[0][0], dados.number_of_people * (-1))
        #print(f'ID Passagem ida: {passagem_ida[0][0]}')

        atualizar_estoque(passagem_volta[0][0], dados.number_of_people * (-1))
        #print(f'ID Passagem volta: {passagem_volta[0][0]}')

        pedido = {
            "id": str(uuid.uuid4()),
            "id_passagem_ida": passagem_ida[0][0],
            "id_passagem_volta": passagem_volta[0][0],
            "numero_pessoas": dados.number_of_people,
            "mensagem": "Passagem reservada com sucesso",
            "cancelado": 0
        }
        salvar_pedido(pedido)
        pedidos_realizados.append(pedido)
        return pedido

# Método para encontrar pedidos na lista pedidos_realizados


def encontrar_pedido(pedido_id):
    for pedido in pedidos_realizados:
        if pedido["id"] == pedido_id:
            return pedido
    return None

# Implementação do serviço CompanhiaAerea definido no .proto


class CompaniaAerea(gRPC_pb2_grpc.CompaniaAereaServicer):
    # Chamado pela Agencia de Viagens para solicitar passagens
    def SolicitarPassagens(self, request, context):
        print('\nProcessando pedido de passagens...')

        if request.HasField("check_out_date"):
            pedido = pedido_ida_volta(request)
        else:
            pedido = pedido_somente_ida(request)

        # Criar o pacote de resposta
        
        #print(f'Pedido: {pedido['id']}')
        if(pedido['id'] != 0):
            resposta = gRPC_pb2.Resposta(
                success=True,
                message='Airline tickets booked successfully',
                reservation_id=str(pedido['id'])
            )
        else:
            resposta = gRPC_pb2.Resposta(
                success=False,
                message=pedido["mensagem"],
                reservation_id='0'
            )

        print(resposta.message)

        print('Pedidos Atuais:')
        for item in pedidos_realizados:
            print(f"    ID pedido: {item['id']}")
            print(f"    ID passagem ida: {item['id_passagem_ida']}")
            print(f"    ID passagem volta: {item['id_passagem_volta']}")
            print(f"    Numero de pessoas: {item['numero_pessoas']}")
            print("    " + "-" * 20)

        return resposta

    # Chamado pela Agencia de Viagens para compensação
    def ReverterPedido(self, request, context):
        global pedidos_realizados
        print(f'\nRevertendo pedido {request.reservation_id}...')

        # encontrando o pedido em pedidos_realizados
        pedido = encontrar_pedido(request.reservation_id)

        if pedido is None:
            resposta = gRPC_pb2.Resposta(
                success=False,
                message=f'Error - Reservation {request.id} not found for compensation',
                reservation_id=str(request.reservation_id)
            )
            return resposta

        # atualizar o estoque
        atualizar_estoque(pedido["id_passagem_ida"], pedido["numero_pessoas"])
        if (int(pedido["id_passagem_volta"]) != 0):
            atualizar_estoque(pedido["id_passagem_volta"],
                              pedido["numero_pessoas"])

        # excluir pedido do banco
        cancelar_pedido(request.reservation_id)

        # colocar pedido em pedidos_revertidos
        pedidos_revertidos.append(pedido)

        # retirar pedido de pedidos_realizados
        pedidos_realizados = [
            p for p in pedidos_realizados if p["id"] != pedido["id"]]

        resposta = gRPC_pb2.Resposta(
            success=True,
            message=f'Airline tickets ID {request.reservation_id} successfully canceled',
            reservation_id=str(request.reservation_id)
        )

        print('Pedidos Atuais:')
        for item in pedidos_realizados:
            print(f"    ID pedido: {item['id']}")
            print(f"    ID passagem ida: {item['id_passagem_ida']}")
            print(f"    ID passagem volta: {item['id_passagem_volta']}")
            print(f"    Numero de pessoas: {item['numero_pessoas']}")
            print("    " + "-" * 20)

        return resposta


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gRPC_pb2_grpc.add_CompaniaAereaServicer_to_server(CompaniaAerea(), server)
    server.add_insecure_port('[::]:50052')
    print("Servidor gRPC rodando na porta 50052...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    buscar_pedidos()
    serve()
