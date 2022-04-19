# 16 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

print('Calculo de Equação de Segundo Grau')

# Recebendo Inputs
a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))

# Verifica se eh uma equacao de segundo grau
if a == 0:
    print('Os valores informados não formam uma Equação de Segundo Grau')
else: 
    # Calculo de Delta
    delta = math.pow(b,2) - (4 * a * c)
    
    if delta < 0:
        print('A Equação não possui valores reais.')
    elif delta == 0:
        print('A Equação possui apenas uma raiz')
        raiz = -b /  (2*a)
        print(f'Raiz: {raiz}')  
    else:
        print(f'A Equação possui duas raizes!')
        raiz_1 = (-b + math.sqrt(delta)) / (2*a)      
        raiz_2 = (-b - math.sqrt(delta)) / (2*a)      
        print(f'Raiz: {raiz_1}') 
        print(f'Raiz: {raiz_2}') 