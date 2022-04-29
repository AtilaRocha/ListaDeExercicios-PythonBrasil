# 28 Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qtn_cds = int(input("Digite a quantidade de CD's : "))
cds = []
n_cd = 1
contador = 0

while contador != qtn_cds:
    print(42*'-')
    print(f'Número do CD: {n_cd}'.center(42))
    valor_cd = cds.append(float(input("Digite o valor do CD: ")))
    n_cd += 1
    contador += 1
    
media = sum(cds) / len(cds)
print(f'Média de cada CD comprado: {media:.2f}')