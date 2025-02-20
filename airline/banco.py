import sqlite3

# Nome do arquivo do banco de dados
# O arquivo será criado no mesmo diretório do script. Use um caminho completo, se necessário.
nome_arquivo_banco = "airline_db.db"

# Conectar ao banco de dados (se não existir, será criado)
conexao = sqlite3.connect(nome_arquivo_banco)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar tabela pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedido (
    id TEXT PRIMARY KEY,
    id_passagem_ida INTEGER NOT NULL,
    id_passagem_volta INTEGER,
    numero_pessoas INTEGER NOT NULL,
    mensagem TEXT,
    cancelado BOOLEAN DEFAULT 0,
    FOREIGN KEY (id_passagem_ida) REFERENCES passagem(id),
    FOREIGN KEY (id_passagem_volta) REFERENCES passagem(id)
)

""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS passagem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origem TEXT NOT NULL,
    destino TEXT NOT NULL,
    data DATETIME NOT NULL,
    estoque INTEGER NOT NULL
);

""")

cursor.execute("""
DELETE FROM passagem
""")

cursor.execute("""
DELETE FROM pedido
""")

# Exemplo: Criar uma tabela
cursor.execute("""
INSERT INTO passagem (origem, destino, data, estoque)
VALUES ('Curitiba', 'Sao Paulo', '2025-06-25 03:00:00', 10)
""")
cursor.execute("""
INSERT INTO passagem (origem, destino, data, estoque)
VALUES ('Sao Paulo', 'Curitiba', '2025-06-30 03:00:00', 10)
""")
cursor.execute("""
INSERT INTO passagem (origem, destino, data, estoque)
VALUES ('Curitiba', 'Rio de Janeiro', '2025-03-20 03:00:00', 10)
""")
cursor.execute("""
INSERT INTO passagem (origem, destino, data, estoque)
VALUES ('Rio de Janeiro', 'Curitiba', '2025-03-30 03:00:00', 10)
""")
cursor.execute("""
INSERT INTO passagem (origem, destino, data, estoque)
VALUES ('Curitiba', 'Fortaleza', '2025-03-25 03:00:00', 10)
""")
cursor.execute("""
INSERT INTO passagem (origem, destino, data, estoque)
VALUES ('Fortaleza', 'Curitiba', '2025-03-29 03:00:00', 10)
""")
cursor.execute("""
INSERT INTO passagem (origem, destino, data, estoque)
VALUES ('Curitiba', 'Paris', '2025-04-12 03:00:00', 10)
""")
cursor.execute("""
INSERT INTO passagem (origem, destino, data, estoque)
VALUES ('Paris', 'Curitiba', '2025-04-20 03:00:00', 10)
""")


# Confirmar as alterações e fechar a conexão
conexao.commit()
conexao.close()

print(f"Banco de dados '{nome_arquivo_banco}' criado com sucesso!")