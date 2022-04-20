# 5 Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacao_A = 0
crescimento_A = 0

while populacao_A <= 0:
    
    populacao_A = int(input('POPULAÇÃO A: '))
    if populacao_A <= 0:
        print('Populacao deve ser um valor positivo')

while crescimento_A <= 0:
    crescimento_A = float(
        input('Informe o percentual de crescimento do pais A: '))
    if crescimento_A <= 0:
        print('Percentual de crescimento deve ser um valor positivo')

populacao_B = populacao_A

while populacao_B <= populacao_A:
    populacao_B = int(input('POPULAÇÃO B: '))
    if populacao_B <= populacao_A:
        print('Populacao do pais B deve ser maior que a populacao do pais A')

crescimento_B = crescimento_A

while crescimento_B >= crescimento_A:
    crescimento_B = float(
        input('Informe o percentual de crescimento do pais B: '))
    if crescimento_B >= crescimento_A:
        print('Percentual de crescimento do pais B deve ser menor que o do pais A')

crescimento_A = 1 + (crescimento_A / 100.0)
crescimento_B = 1 + (crescimento_B / 100.0)

anos = 1
while populacao_A <= populacao_B:
    populacao_A *= crescimento_A
    populacao_B *= crescimento_B
    anos += 1

print(f'Serao necessarios {anos} anos para que a populacao do pais A ultrapasse a populacao do pais B')