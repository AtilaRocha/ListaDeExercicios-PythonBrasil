# 8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


n1 = float(input('Digite o valor do primeiro produto: '))
n2 = float(input('Digite o valor do segundo produto: '))
n3 = float(input('Digite o valor do terceiro produto: '))

if n1 < n2 and n1 < n3:
    print(f'o primeiro produto é o mais barato custando: {n1}')
    
if n2 < n1 and n2 < n3:
    print(f'o segundo produto é o mais barato custando: {n2}')
    
if n3 < n1 and n3 < n2:
    print(f'o terceiro produto é o mais barato custando: {n3}')







