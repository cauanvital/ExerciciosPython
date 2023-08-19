# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metq = float(input("Insira o tamanho da parede a ser pintada em metros quadrados:   "))
litn = metq / 3
latn = round(litn / 18 + 0.5, 0)
valp = latn * 80
print(f"Você precisará de {latn:.0f} latas de tinta, gastando R${valp:.2f}")
