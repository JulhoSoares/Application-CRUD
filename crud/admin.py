from db import cursor,conexao

def menu_admin():
     while True:
        opcao = input("1-Inserir, 2-Deletar, 3-Consultar, 4-Voltar Autenticar, 0-Sair, : ")
        if opcao == "1":
            nome = input("Nome: ")
            codigo = input("Código: ")
            cursor.execute("INSERT INTO usuario (nome, codigo) VALUES (%s, %s)", (nome, codigo))
            conexao.commit()
            print("Inserido com sucesso.")
        elif opcao == "2":
            try:
                id = int(input("ID para excluir: "))
                cursor.execute("DELETE FROM usuario WHERE id=%s", (id,))
                conexao.commit()
                print("Excluído.")
            except ValueError:
                print("ID inválid, tente novamente")
        elif opcao == "3":
            print("TABELA DE USUARIOS COMUNS")
            cursor.execute("SELECT * FROM usuario")
            for linha in cursor.fetchall():
                print(linha)
            print("TABELA DO ADMINISTRADOR")
            cursor.execute("SELECT * FROM usuarios")
            for linha in cursor.fetchall():
                print(linha)
        elif opcao =="4":
            #usuario = autenticar()
            #resul=menu_usuario()
            return "voltar"
        elif opcao == "0":
            print("FIM DO PROGRAMA")
            return "sair"
        else:
            print('!! OPÇÃO INVÁLIDA !!')