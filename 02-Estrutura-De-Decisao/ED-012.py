# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
# os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#   No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

vh = float(input("Insira o valor da hora de trabalho:   "))
qh = float(input("Insira a quantidade de horas trabalhadas no mês:   "))
salb = vh * qh
ir = None

if salb <= 900:
    ir = 0
elif 900 < salb <= 1500:
    ir = 5
elif 1500 < salb <= 2500:
    ir = 10
elif salb > 2500:
    ir = 20

dest = salb / 100 * (ir + 10)

print(f"Salário Bruto: R${salb:.2f}")
print(f"(-) IR ({ir}%): R${salb / 100 * ir:.2f}")
print(f"(-) INSS (10%): R${salb / 100 * 10:.2f}")
print(f"FGTS (11%): R${salb / 100 * 11:.2f}")
print(f"Total de descontos: R${dest:.2f}")
print(f"Salário Liquido: R${salb - dest:.2f}")
