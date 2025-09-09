import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",       # ou 127.0.0.1
    user="root",            # ou outro usuário
    password="",            # sua senha
    database="bancodate"     # nome do banco
)

cursor = conexao.cursor()
