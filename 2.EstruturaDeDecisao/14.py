# 14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota_1 = float(input('Informe o valor da primeira nota: '))
nota_2 = float(input('Informe o valor da segunda nota: '))

media = (nota_1 + nota_2) / 2
print()
if media <= 4:
    print(f'Conceito: E')
    aprovado = False
elif media <= 6:
    print(f'Conceito: D')
    aprovado = False
elif media <= 7.5:
    print(f'Conceito: C')
    aprovado = True
elif media <= 9:
    print(f'Conceito: B')
    aprovado = True
else:
    print(f'Conceito: A')
    aprovado = True
print()
if (aprovado):
    print('APROVADO')
else:
    print('REPROVADO')