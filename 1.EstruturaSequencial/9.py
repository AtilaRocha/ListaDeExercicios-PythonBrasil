# 9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

f = float(input('Qual a temperatura em Farenheit: '))

c = 5 * (f - 32) / 9


print(f'A temperatura em celsius é {c:.2f}Cº!')