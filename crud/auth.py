from db import cursor

def autenticar():
    login = input("Usuário:")
    senha_hash = input("Senha: ")
    cursor.execute("SELECT * FROM tabela_adm WHERE login=%s AND senha_hash=%s", (login, senha_hash))
    resultado = cursor.fetchone()
    if resultado:
        return {"id": resultado[0], "login": resultado[2], "tipo": resultado[4]}  # tipo = admin ou comum
    else:
        return None
