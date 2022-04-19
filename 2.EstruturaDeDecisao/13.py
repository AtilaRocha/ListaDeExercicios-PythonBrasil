# 13 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_numero = int(input('DIGITE UM NÚMERO DO DIA DA SEMANA PARA SABER O NOME DO DIA: '))

if dia_numero == 1:
    print(f'O NÚMERO {1} CORRESPONDE A DOMINGO!')
elif dia_numero == 2:
    print(f'O NÚMERO {2} CORRESPONDE A SEGUNDA!')
elif dia_numero == 3:
    print(f'O NÚMERO {3} CORRESPONDE A TERÇA!')
elif dia_numero == 4:
    print(f'O NÚMERO {4} CORRESPONDE A QUARTA!')
elif dia_numero == 5:
    print(f'O NÚMERO {5} CORRESPONDE A QUINTA!')
elif dia_numero == 6:
    print(f'O NÚMERO {6} CORRESPONDE A SEXTA!')
elif dia_numero == 7:
    print(f'O NÚMERO {7} CORRESPONDE A SABADO!')
else:
    print('VALOR INVALIDO!')