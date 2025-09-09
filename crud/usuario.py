from db import cursor, conexao

def menu_usuario():
    while True:
        opcao = input("1-Inserir, 2-Consultar, 3-Voltar Autenticar, 0-Sair: ")

        if opcao == "1":
            try:
                nome = input("Nome: ")
                codigo = input("Código: ")
                cursor.execute(
                    "INSERT INTO usuario (nome, codigo) VALUES (%s, %s)",
                    (nome, codigo)
                )
                conexao.commit()
                print("Inserido com sucesso.")
            except Exception as e:
                print("Erro ao inserir:", e)

        elif opcao == "2":
            print("TABELA DE USUÁRIOS COMUNS")
            cursor.execute("SELECT * FROM usuario")
            for linha in cursor.fetchall():
                print(linha)

        elif opcao == "3":
            return "voltar"

        elif opcao == "0":
            print("FIM DO PROGRAMA")
            return "sair"

        else:
            print("!! OPÇÃO INVÁLIDA !!")
