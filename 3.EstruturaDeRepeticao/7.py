# 7 Faça um programa que leia 5 números e informe o maior número.

for i in range(0, 5):
    numero = int(input('Informe um numero: '))
    if 'maior' in vars():
        if numero > maior:
            maior = numero
    else:
        maior = numero

print(f'O maior numero que voce digitou é: {maior}')