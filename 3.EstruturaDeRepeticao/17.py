# 17 Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

import numpy
n_fato = int(input('Digite o número para fatoração:'))
numeros = list()
print(f'Calculando fatoração do número {n_fato}:')
for n in range(n_fato, 1, -1):
    print(f'{n}', end=' x ')
    numeros.append(n)
print('1 = ', end='')
print(f'{numpy.prod(numeros)}')