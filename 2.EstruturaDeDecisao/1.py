# 1 Faça um Programa que peça dois números e imprima o maior deles.
a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))

if a > b:
    print(f'O maior valor digitado é {a:.2f}')
elif a == b:
    print(f'Ambos os valores são iguais.')
else:
    print(f'O maior valor é {b:.2f}')
