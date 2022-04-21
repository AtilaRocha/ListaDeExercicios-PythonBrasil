# 25 Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n_alunos = int(input('Número de Alunos: '))
lista_alunos = []

for i in range(n_alunos):     
    idade = lista_alunos.append(int(input("Digite a idade do Aluno: ")))
if sum(lista_alunos) / len(lista_alunos) < 25:
        print(f'A turma é JOVEM.')
elif sum(lista_alunos) / len(lista_alunos) >= 25 and sum(lista_alunos) / len(lista_alunos) < 60:
        print(f"A turma é ADULTA.")
else:
        print('A turma é IDOSA.')