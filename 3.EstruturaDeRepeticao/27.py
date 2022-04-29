# 27 Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input("Número de Turmas: "))
alunos_turmas = []
turma = 1
contador = 0

while contador != turmas:
    print(42*'-')
    print(f'TURMA {turma}'.center(42))
    alunos = int(input("Alunos da turma : "))
    while alunos > 40 or alunos < 1:
        print(f'Turma: {turma}\n[ERRORR01] - Uma turma precisa ter entre 1 a 40 alunos.')
        alunos = int(input("Alunos da turma : "))        
    turma += 1
    contador += 1
print(42*'-')
alunos_turmas.append(alunos)
media = sum(alunos_turmas) / len(alunos_turmas)
print(f'Media de alunos por turma: {media:.0f}'.center(42))