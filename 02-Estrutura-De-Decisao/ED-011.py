# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
# o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
#       salários até R$ 280,00 (incluindo) : aumento de 20%
#       salários entre R$280,00 e R$700,00: aumento de 15%
#       salários entre R$700,00 e R$1500,00: aumento de 10%
#       salários de R$1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:
#           -salário antes do reajuste;
#           -percentual de aumento aplicado;
#           -valor do aumento;
#           -novo salário após o aumento.

sal = float(input("Insira o valor do seu salário:   "))

print(f"Salário antes do reajuste: R${sal:.2f}")
if sal <= 280:
    aum = sal / 100 * 20
    print("Percentual de aumento aplicado: 20%")
    print(f"Valor do aumento: R${aum:.2f}")
    print(f"Novo salário após o aumento: R${sal + aum:.2f}")
elif 280 < sal <= 700:
    aum = sal / 100 * 15
    print("Percentual de aumento aplicado: 15%")
    print(f"Valor do aumento: R${aum:.2f}")
    print(f"Novo salário após o aumento: R${sal + aum:.2f}")
elif 700 < sal <= 1500:
    aum = sal / 100 * 10
    print("Percentual de aumento aplicado: 10%")
    print(f"Valor do aumento: R${aum:.2f}")
    print(f"Novo salário após o aumento: R${sal + aum:.2f}")
elif sal > 1500:
    aum = sal / 100 * 5
    print("Percentual de aumento aplicado: 5%")
    print(f"Valor do aumento: R${aum:.2f}")
    print(f"Novo salário após o aumento: R${sal + aum:.2f}")
else:
    print("bruh")
