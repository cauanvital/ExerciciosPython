# Utilize uma lista para resolver o problema a seguir. Uma empresa paga os seus vendedores com base em comissões. O
# vendedor recebe $200 por semana mais 9 por cento das suas vendas brutas daquela semana. Por exemplo, um vendedor que
# teve vendas brutas de $3000 numa semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva
# um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
# intervalos de valores:
#       $200 - $299
#       $300 - $399
#       $400 - $499
#       $500 - $599
#       $600 - $699
#       $700 - $799
#       $800 - $899
#       $900 - $999
#       $1000 em diante

cont = 1
salarioVendedor = []
qtdVendeComissao = {}
cheqMedia = [200]

while True:
    j = float(input(f"Insira as vendas do vendedor {cont} (digite \"0\" para finalizar): "))
    if j == 0:
        break
    salarioVendedor.append(j / 100 * 9 + 200)
    cont += 1

maiorSalario = round(max(salarioVendedor)) // 100 - 1

for i in range(maiorSalario):

    for j in salarioVendedor:
        if cheqMedia[i] + 100 > j > cheqMedia[i]:
            try:
                qtdVendeComissao[cheqMedia[i]] += 1
            except KeyError:
                qtdVendeComissao[cheqMedia[i]] = 1

    cheqMedia.append(cheqMedia[i] + 100)

print()
for i in qtdVendeComissao:
    print(f"Quantidade de vendedores com salário entre {i} e {i + 100}: {qtdVendeComissao[i]}")
