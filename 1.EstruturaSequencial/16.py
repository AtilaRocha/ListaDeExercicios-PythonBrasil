# 16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

t = float(input('ÁREA DA PINTURA(EM METROS²): '))

l = t / 3
latas = int(l/18)

if l % 18 != 0:
    latas += 1
    
print(f'NÚMERO DE LATAS: {latas:.2f}')
valor_total = latas * 80
print(f'VALOR DA COMPRA: {valor_total:.2f}')












