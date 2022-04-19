# 20 Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota_1 = float(input('Digite a Primeira nota do Aluno: ')) 
nota_2 = float(input('Digite a Segunda nota do Aluno: ')) 
nota_3 = float(input('Digite a Terceira nota do Aluno: ')) 

media = (nota_1 + nota_2 + nota_3) / 3

print(f'MÉDIA DO ALUNO: {media}')
if media == 10:
    print('APROVADO COM DINSTINÇÃO')
elif media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')