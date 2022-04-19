# 28 O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
 
def loja():
    # Menu de Opções
    print(42 * '-')
    print('MENU PRINCIPAL'.center(42))
    print(42 * '-')
    print(' 1 - File Duplo')
    print(' 2 - Alcatra')
    print(' 3 - Picanha')
    print(42 * '-')
    tipo_Carne = str(input('Informe o tipo da carne escolhida: '))

    # Escolha da quantidade
    qtd = float(input('Informe a quantidade comprada (KG): '))

    # Verifica cartao
    cartao_Atacadao = str(input('Usará cartao Atacadão (S/N): ')).upper()

    print(42 * '-')
    print('CUPOM FISCAL'.center(42))
    print(42 * '-')

    # Verifica o tipo da carne e calcula o valor bruto
    if tipo_Carne == '1':
        print('Carne Escolhida: File Duplo')
        if qtd <= 5:
            valorBruto = qtd * 4.9
        else:
            valorBruto = qtd * 5.8
    elif tipo_Carne == '2':
        print('Carne Escolhida: Alcatra')
        if qtd <= 5:
            valorBruto = qtd * 5.9
        else:
            valorBruto = qtd * 6.8
    else:
        print('Carne Escolhida: Picanha')
        if qtd <= 5:
            valorBruto = qtd * 6.9
        else:
            valorBruto = qtd * 7.8
    print(f'Valor Bruto deu: R$ {valorBruto:.2f}')

    # Verifica se possui desconto
    desconto = 0.0
    if cartao_Atacadao in 'S':
        print('Pagamento com Cartao Atacadão')
        desconto = valorBruto * 0.05
    else:
        print('Pagamento NÃO sera com o cartao Tabajara')

    print(F'Desconto: {desconto:.2f}')
    print(f'Valor a Pagar: {valorBruto - desconto:.2f}')
    print(42*'-')
    
loja()