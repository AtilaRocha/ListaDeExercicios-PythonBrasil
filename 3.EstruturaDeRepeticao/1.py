# 1 Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# Criando acumulador
nota = 0

# Analisando se a nota é valida 
while nota < 0 or nota > 10:
    nota = int(input('Informe uma nota: '))
    if nota < 0 or nota > 10:
        print('Nota Invalida')
