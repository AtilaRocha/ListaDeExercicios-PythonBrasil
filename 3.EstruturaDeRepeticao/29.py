# 29 O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

produtos = int(input("Número de produtos tabelados: "))
while produtos > 50 or produtos < 1:
    produtos = int(input("[ERROR01] O número de produtos deve ser entre 1 e 50!\n Número de Produtos: "))

precos = []
n_produto = 1
count = 0

print(42*'-')
for i in range(produtos):
    print(f'Produto {n_produto}'.center(42))
    preco = precos.append(float(input("Preço: ")))
    n_produto += 1

n_produto = 1
print(42*'-')
print('TABELA DE PRODUTOS'.center(42))
for j in range(produtos):
    print(f'Produto {n_produto}: {precos[count]}')
    count += 1
    n_produto += 1
print(42*'-')