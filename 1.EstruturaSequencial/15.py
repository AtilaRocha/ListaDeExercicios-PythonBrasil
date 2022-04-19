# 15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# A) salário bruto.
# B) quanto pagou ao INSS.
# C) quanto pagou ao sindicato.
# D) o salário líquido.
# E) calcule os descontos e o salário líquido, conforme a tabela abaixo:

"""+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

print('-' *30)

valor_hora = float(input('QUANTO GANHA POR HORA: '))
hora_trabalhada = float(input('QUNTAS HORAS TRABALHADAS NO MÊS: '))


salario_bruto = valor_hora * hora_trabalhada
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print('~' *30)
print(f'Salario Bruto: {salario_bruto:.2f}$')
print(f'Imposto de Renda: {imposto_renda:.2f}$')
print(f'INSS: {inss:.2f}$')
print(f'Sindicato: {sindicato:.2f}$')
print(f'Salario Liquido: {salario_liquido:.2f}$')
print('~' *30)









