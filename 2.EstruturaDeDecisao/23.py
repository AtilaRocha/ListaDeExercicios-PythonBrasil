# 23 Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

valor = float(input('Informe um numero: '))

if valor == int(valor):
    print('Valor eh inteiro')
else:
    print('Valor eh decimal')