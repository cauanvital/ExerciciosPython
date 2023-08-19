# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#       salário bruto.
#       quanto pagou ao INSS.
#       quanto pagou ao sindicato.
#       o salário líquido.
#       calcule os descontos e o salário líquido, conforme a tabela abaixo:
#           + Salário Bruto : R$
#           - IR (11%) : R$
#           - INSS (8%) : R$
#           - Sindicato ( 5%) : R$
#           = Salário Liquido : R$
#   Obs.: Salário Bruto - Descontos = Salário Líquido.

vho = float(input("Insira quanto você ganha por hora:   "))
hme = float(input("Insira a quantidade de horas trabalhadas no mês:   "))
salb = vho * hme
ir = salb / 100 * 11
inss = salb / 100 * 8
sind = salb / 100 * 5
sall = salb - ir - inss - sind

print(f"+ Salário Bruto: R${salb:.2f}")
print(f"- IR (11%): R${ir:.2f}")
print(f"- INSS (8%): R${inss:.2f}")
print(f"- Sindicato (5%): R${sind:.2f}")
print(f"= Salário Liquido: R${sall:.2f}")
