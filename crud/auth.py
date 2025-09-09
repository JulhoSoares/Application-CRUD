from db import cursor
def autenticar():
    login = input("Usuário:")
    senha = input("Senha: ")
    cursor.execute("SELECT * FROM usuarios WHERE login=%s AND senha=%s", (login, senha))
    resultado = cursor.fetchone()

    if resultado:
        return {"id": resultado[0], "login": resultado[2], "tipo": resultado[4]}  # tipo = admin ou comum
    else:
        return None