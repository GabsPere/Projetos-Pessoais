#  Inserindo dados na tabela através de operações DML

import sqlite3

# 1 -> Conectando no banco de dados
'''
PS: O comando 'connect' quando não existe um banco de dados ele cria, mas
quando existe um BD serve para fazer a conexão.
'''
conexao = sqlite3.connect("jogos.db") # -> Conectando no banco de dados.

# 2 -> Inserindo dados pelo input
name = input("Digite o nome do jogo: ")
price = float(input("Digite o preço: "))

# 3-> Criando um cursor
'''
Um cursor é um interador que permite navegar e
manipular os registros de um BD (DML ou DDL).
'''
cursor = conexao.cursor()

# 4 -> Inserindo dados
cursor.execute("""
    INSERT INTO games(name,price)
    VALUES(?,?)
""",(name,price))

# 5 -> Gravando dados no DB (database)
conexao.commit()
print("Dados inseridos com sucesso!")

# 5 -> Fechando conexão
conexao.close()