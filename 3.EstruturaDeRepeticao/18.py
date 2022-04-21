# 18 Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista = []
contador = 0
total = int(input("Digite total de números desejados: "))

while total != contador:
        n = lista.append(float(input('\nDigite um valor: ')))
        contador += 1
print(42*'-')
print(f' Lista: {lista}\n Maior: {max(lista)}\n Menor: {min(lista)}\n Soma: {max(lista)+min(lista)}')