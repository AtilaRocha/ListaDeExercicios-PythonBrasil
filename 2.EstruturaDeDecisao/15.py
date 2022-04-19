# 15 Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

print('INFORME OS VALORES DOS LADOS DO TRIANGULO')
a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
print()
# Verifica se eh um triangulo
if a > (b+c) or b > (a+c) or c > (a+b):
    triangulo = False
    
else: triangulo = True

if triangulo:
    print(f'Os valores formam um Triangulo')
    print()
    # Verifica o tipo de triangulo
    if a == b and b == c:
        print(f'Triangulo Equilatero!')
    elif a == b or a == c or b == c:
        print('Triangulo Isosceles!')
    else:
        print(f'Triangulo Escaleno!')
else:
    print('Os valores informados não formam um Triangulo')