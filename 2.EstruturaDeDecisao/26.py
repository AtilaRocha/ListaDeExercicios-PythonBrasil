# 26 Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 

# Coletando inputs
Combustivel_class = str(input('Informe (A) para Alcool ou (G) para Gasolina: ')).upper()
Litros_total = float(input('Informe a quantidade de litros: '))

# Define o valor e os descontos - Valor verificado em 20/04/22

if Combustivel_class == 'A':
    valor = 5.6
    if Litros_total <= 20:
        desconto = 3
    else:
        desconto = 5

else:
    valor = 6.39
    if Litros_total <= 20:
        desconto = 4
    else:
        desconto = 6
        
# Calcula o total
Pagamento_total = (valor * Litros_total) * ((100 - desconto) / 100.0)

print (f'Total a pagar: R$ {Pagamento_total:.2f}')