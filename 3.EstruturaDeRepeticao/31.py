# 31 O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

# Número de produtos para compra
produtos = int(input("Número de Produtos: "))

# Acumuladores
precos = soma = []
n_produto = 1
count = 0
a = 0.0


print(42*'-')
for i in range(produtos):
    print(f'Produto {n_produto}'.center(42))
    preco = precos.append(float(input("Preço: ")))
    n_produto += 1
    soma = sum(precos)
    
n_produto = 1
print(42*'-')
print('NOTA FISCAL'.center(42))
for j in range(produtos):
    print(f'Produto {n_produto}: R$ {precos[count]}')
    count += 1
    n_produto += 1
print(f'TOTAL: R$ {soma}')
print(42*'-')

# Pagamento e troco
pagamento = float(input('Valor pago: '))
troco = pagamento - soma
print(f'O troco do valor pago será: R$ {troco:.2f}')