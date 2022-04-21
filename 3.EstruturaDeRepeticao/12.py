# 12 Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 10 = 50

def tabuada():
    # Coletando Inputs
    n = int(input("Digite um número (1 à 10): "))
    cont = 1

    while cont <= 10:
        tab = n * cont
        print(f'{n} X {cont} = {tab}')
        cont = cont + 1
tabuada()