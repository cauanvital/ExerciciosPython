# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#       Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#           -comprar apenas latas de 18 litros;
#           -comprar apenas galões de 3,6 litros;
#           -misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
#           arredonde os valores para cima, isto é, considere latas cheias.

metq = float(input("Insira o tamanho em metros quadrados da parede a ser pintada:   "))
litn = round(metq / 6 + (metq / 6 / 100 * 10), 1)

# Variáveis para calcular valor comprando apenas latas de 18 litros
latn = round(litn / 18 + 0.5)
vall = latn * 80

# Variáveis para calcular valor comprando apenas galões de 3,6 litros
galn = round(litn / 3.6 + 0.5)
valg = galn * 25

# Variáveis para calcular valor comprando ambos, galões e latas
latm = round(litn / 18 - 0.5)
dif = litn - (latm * 18)
galm = round(dif / 3.6 + 0.5)
valt = (latm * 80) + (galm * 25)

print(f"Litros necessários: {litn}")
print(f"Comprando apenas latas de 18 litros, serão necessárias {latn} latas, custando R${vall:.2f} ao todo")
print(f"Comprando apenas galões de 3,6 litros, serão necessários {galn} galões, custando R${valg:.2f} ao todo")
print(f"Comprando tudo misturado, serão necessários {latm} latas e {galm} galões, custando R${valt:.2f} ao todo")
