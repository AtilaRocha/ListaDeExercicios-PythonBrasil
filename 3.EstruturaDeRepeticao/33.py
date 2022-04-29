# 33 O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

# Número de n_temp para compra
n_temps = int(input("Número de Temperaturas: "))

# Acumuladores
temperaturas = []
n_temp = 1


# Input das Tempse analise
print(42*'-')
for i in range(n_temps):
    print(f'Temperratura {n_temps}'.center(42))
    temp = temperaturas.append(float(input("Temperatura: ")))
    n_temp += 1
media = sum(temperaturas) / len(temperaturas)

# Mostrando temperaturas 
print(f'Maior Temperatura: {(max(temperaturas))}°C\nMenor Temperatura: {min(temperaturas)}°C\nMédia das Temperaturas: {media}°C')