# 24 Faça um programa que calcule o mostre a média aritmética de N notas.

n_notas = int(input("NÚMERO DE NOTAS A SEREM DIGITADAS: "))
contador = 0
notas_total = []

while contador < n_notas:
        notas = notas_total.append(float(input("DIGITE A NOTA: ")))
        contador += 1
media = sum(notas_total) / n_notas
print(f'MÉDIA: {media:.2f}')     