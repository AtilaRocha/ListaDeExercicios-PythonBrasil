# 2 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

def senha_user():
    while True:
        # Coletando Inputs
        user = input('Informe um nome de usuario: ')
        senha = input('Informe a senha: ')
        # Analisando igualdade
        if user == senha:
            print(f'A senha nao pode ser igual ao nome do usuario')
senha_user()
