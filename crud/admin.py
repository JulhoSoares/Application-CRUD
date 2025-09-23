import bcrypt

from db import cursor,conexao

def menu_admin():
     while True:
        opcao = input("1-Inserir, 2-Deletar, 3-Consultar, 4-Voltar Autenticar, 0-Sair, : ")
        if opcao == "1":
            nome = input("Nome :")
            senha=input("Digite uma senha! :")
            codigo = input("Código: ")

            hash=bcrypt.hashpw(senha.encode("utf-8"),bcrypt.gensalt())
            cursor.execute("INSERT INTO usuario (nome,hash,codigo) VALUES (%s, %s,%s)", (nome, hash, codigo))
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
            cursor.execute("SELECT * FROM tabela_adm")
            for linha in cursor.fetchall():
                print(linha)
        elif opcao =="4":
            return "voltar"
        elif opcao == "0":
            print("FIM DO PROGRAMA")
            return "sair"
        else:
            print('!! OPÇÃO INVÁLIDA !!')
