# 12 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

# Inputs dos dados
pagamento_hora = float(input('Informe o valor da hora trabalhada: '))
hora_total = float(input('Informe a quantidade de horas trabalhadas no mes:'))

# Calcula o salario bruto
salario_raw = pagamento_hora * hora_total

# Calcula o imposto de renda
if salario_raw > 2500:
    IR_aliquota = 20
elif salario_raw > 1500:
    IR_aliquota = 10
elif salario_raw > 900:
    IR_aliquota = 5
else:
    IR_aliquota = 0

Pagamento_IR = salario_raw * (IR_aliquota / 100)

# Calcula o valor para o sindicato
Sindicato_pagamento = salario_raw * (3 / 100.0)

# Calcula o total de descontos
totalDescontos = Pagamento_IR + Sindicato_pagamento

# Calcula o valor do FGTS
valorFGTS = salario_raw * (11 / 100.0)

# Calcula o salario liquido
salarioLiquido = salario_raw - totalDescontos

# Resultados

print(f'Salario Bruto ({pagamento_hora}*{hora_total}): R${salario_raw:.2f}')
print(f'(-) IR {IR_aliquota}%: R${Pagamento_IR:.2f}')
print(f'(-) Sindicato (3%): R${Sindicato_pagamento:.2f}')
print(f'FGTS (11%): R${valorFGTS:.2f}')
print(f'Total de Descotnos: R${totalDescontos:.2f}')
print(f'Salario Liquido: R${salarioLiquido:.2f}')