# 14 Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

lista = []
par = 0
impar = 0

for i in range(0,10):
    a = [int(input('\nDigite um número: '))] 
    lista += a
   
print(50*'~')
print(lista)
print(50*'~')

for value in lista:
    if value % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f' Par: {par}\n Impar: {impar}')