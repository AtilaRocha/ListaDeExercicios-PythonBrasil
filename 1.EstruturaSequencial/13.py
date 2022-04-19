# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# A) Para homens: (72.7*h) - 58
# B) Para mulheres: (62.1*h) - 44.7

print()
s = input('Qual seu sexo (M/F) ? ').upper
a = float(input('Qual sua altura (em metros) ? '))
p = float(input('Qual seu peso (em kg) ? '))

if s == 'M':
    peso_ideal = (72.7 * a) - 58
else:
    peso_ideal = (62.1 * a) - 44.7

print()

if p > peso_ideal:
    print(f'Voce esta acima do seu peso ideal: {peso_ideal:.2f}')

elif p < peso_ideal:
    print(f'Voce esta abaixo do seu peso ideal: {peso_ideal:.2f}')

else:
    print(f'Voce esta no seu peso ideal: {peso_ideal:.2f}')
print()









