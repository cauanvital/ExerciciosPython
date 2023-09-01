# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
# dos juros, quantidade de parcelas e valor da parcela.
#       Os juros e a quantidade de parcelas seguem a tabela abaixo:
#       Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#           1       0
#           3       10
#           6       15
#           9       20
#           12      25
#       Exemplo de saída do programa:
#       Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#           R$ 1.000,00     0               1                       R$  1.000,00
#           R$ 1.100,00     100             3                       R$    366,00
#           R$ 1.150,00     150             6                       R$    191,67

valorDivida = float(input("Insira o valor da dívida: "))
valParcela = valorDivida
taxaJuros = 10
qtdParcela = 1
valJuros = 0

print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")

for i in range(5):
    if i != 0:
        valJuros = valorDivida / 100 * taxaJuros
        taxaJuros += 5
    else:
        valJuros = 0

    novaDivida = valJuros + valorDivida
    valParcela = novaDivida / qtdParcela

    print(f"R$ {novaDivida:.2f}", " " * (7 - (len(f"{novaDivida:.2f}") - 4)),
          f"| R$ {valJuros:.2f}", " " * (15 - len(f"{valJuros:.2f}") - 4),
          f"| {qtdParcela}", " " * (17 - (len(f"{qtdParcela}") - 4)),
          f"| R$ {valParcela:.2f}")

    valorDivida = float(valorDivida)
    valJuros = float(valJuros)
    qtdParcela = qtdParcela + 2 if i == 0 else qtdParcela + 3
