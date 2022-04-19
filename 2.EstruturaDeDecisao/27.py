# 27 Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Coletando Inputs
morangos = float(input('Informe a quantidade de morangos comprados (KG): '))
macas = float(input('Informe a quantidade de macas comprados (KG): '))

# Valor RAW dos produtos
if morangos <= 5:
    Morangos_raw = morangos * 2.5
else:
    Morangos_raw = morangos * 2.2

if macas <= 5:
    Macas_raw = macas * 1.8
else:
    Macas_raw = macas * 1.5

Valor_raw = Morangos_raw + Macas_raw

# Calculando descontos
if (morangos + macas) >= 8 or Valor_raw >= 25:
    Valor_raw = Valor_raw * 0.9

print(f'Valor a pagar: R${Valor_raw:.2f}')