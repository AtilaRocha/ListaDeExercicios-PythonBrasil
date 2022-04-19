# 9 Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
num3 = int(input('Informe mais um numero: '))


if num1 >= num2 and num1 >= num3:
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
        
        
elif num2 >= num3:
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
        
        
else:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)












