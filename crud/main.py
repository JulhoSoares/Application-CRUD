from auth import autenticar
from admin import menu_admin
from usuario import menu_usuario
while True:
    usuario = autenticar()
    if usuario:
        if usuario['tipo'] == 'admin':
            resultado = menu_admin()
            if resultado == "voltar":
                continue
            elif resultado =="sair":
                break
        else:
            resultado = menu_usuario()
            if resultado =="voltar":
                continue
            elif resultado =="sair":
                break
    else:
        print("Login falhou.")