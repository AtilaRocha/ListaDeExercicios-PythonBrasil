# 26 Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

# Número de eleitores para votação
eleitores = int(input("Digite o número de eleitores: "))

# Criando acumuladores
votos = voto = [] 
contador = 0

# Analisando votos
while contador != eleitores:
    
    voto = [int(input("Qual candidato deseja votar? \n Candidado[1]\n Candidato[2] \n Candidato[3] \nSEU VOTO: "))]
    
    verifica_candidato = 1 in voto or 2 in voto or 3 in voto
    if verifica_candidato == True:
        print('')
        votos.append(voto)
        contador += 1
    else:
        voto = [int(input('NÃO EXISTE ESTE CANDIDATO, POR GENTILEZA DIGITE UM CANDIDATO VALIDO!\n Candidado[1]\n Candidato[2] \n Candidato[3]\nSEU VOTO:'))]

# Exibindo resultado
print(42*'-')
print(votos)
print("Quantidade de votos para candidato 1: ", votos.count([1]))
print("Quantidade de votos para candidato 2: ", votos.count([2]))
print("Quantidade de votos para candidato 3: ", votos.count([3]))
print(42*'-')