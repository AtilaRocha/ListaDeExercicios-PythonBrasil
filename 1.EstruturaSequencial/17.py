# 17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

print('~' * 50)
t = float(input('ÁREA DA PINTURA(EM METROS²): '))
print('~' * 50)
l = (t / 6.0) * 1.1  # 10% de folga
latas = int(l / 18.0)
galoes = int(l / 3.6)

# Calculando número de latas
if l % 18 != 0:
    latas += 1

# Calculando número de galões
if l % 3.6 != 0:
    galoes += 1

# Calculando a mistura de latas e galões

mix_latas = int(l / 18 )
mix_galoes = int((l - (mix_latas * 18))/ 3.6)

if ((l - (mix_latas * 18) % 3.6 !=0 )):
    mix_galoes += 1
    
# valor_latas = latas * 80

print('-'*20+'VALORES'+'-'*20)

print(f'{latas} LATAS: {latas * 80:.2f}$')
print(f'{galoes} GALÕES: {galoes * 25:.2f}$')
print(f'{mix_latas} MISTURAS DE LATAS E {mix_galoes} GALÕES MISTURADOS: {(mix_latas * 80) + (mix_galoes * 25):.2f}$')


print('~' * 50)