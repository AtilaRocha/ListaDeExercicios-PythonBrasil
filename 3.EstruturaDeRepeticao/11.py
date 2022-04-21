# 11 Altere o programa anterior para mostrar no final a soma dos números.

# Coletando Inputs
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

# Analisando o range
for i in range(n1 + 1, n2):
        print(i)

for i in range(n2 + 1, n1):
        print(i)

# Somando números
x = lambda i: i ++ i

print(f'Soma dos Números: {x(i)}' )