# 20 Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menor que 16.

import math
lista = []
contador = 0
total = int(input("Digite quantos números quer calcular o fatorial: "))
print(42*'-')
while total != contador:
    numero = int(input("\nDigite um número: "))
    while numero>16 or numero<0 or numero // 1 != numero:
        numero = int(input("\n [ERROR01]\nPor gentileza, digite um número inteiro, positivo e menor que 16: "))
    print(f"FATORIAL: {(math.factorial(numero))}")
    contador += 1 
print(42*'-')   