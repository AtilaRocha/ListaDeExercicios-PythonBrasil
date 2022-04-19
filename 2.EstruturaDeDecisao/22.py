# 22 Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

valor = int(input('DIGITE UM VALOR: '))

if valor % 2 == 0:
    print('O NÚMERO DIGITADO É PAR')
else:
    print('O NÚMERO DIGITADO É IMPAR')