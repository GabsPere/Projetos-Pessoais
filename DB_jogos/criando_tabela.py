# 4 -> Criando tabela de jogos para armazenar os dados

import sqlite3

conexao = sqlite3.connect("jogos.db")

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE games(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               price REAL NOT NULL
    );
""")