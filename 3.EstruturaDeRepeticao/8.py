# 8 Faça um programa que leia 5 números e informe a soma e a média dos números.

# Criandoa Acumulador
soma = 0

# Calculando
for n in range(0, 5):
    numero = int(input('Informe um número: '))
    soma += numero
    media = soma/5
print(f'A soma dos numeros é: {soma}')
print(f'A media dos numeros é: {media:.2f}')