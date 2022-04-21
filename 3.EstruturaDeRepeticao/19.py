# 19 Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista = []
contador = 0

total = int(input("Digite total de números desejados: "))
while total != contador:
    numero = float(input("\nDigite um número: "))

    while numero > 1000 or numero < 0:
        numero = float(input("\n [ERROR01]\nPor gentileza digite um número entre 0 e 1000: "))
    lista.append(numero)
    contador += 1
print(42*'-')
print(f' Lista: {lista}\n Maior: {max(lista)}\n Menor: {min(lista)}\n Soma: {max(lista)+min(lista)}')