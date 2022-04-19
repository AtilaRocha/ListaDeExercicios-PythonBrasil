# 6 Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Digite o primerio número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'{n1}')
    
if n2 > n1 and n2 > n3:
    print(f'{n2}')
    
if n3 > n1 and n3 > n2:
    print(f'{n3}')








