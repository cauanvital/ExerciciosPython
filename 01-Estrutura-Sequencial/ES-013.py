# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#       Para homens: (72.7*h) - 58
#       Para mulheres: (62.1*h) - 44.7

h = float(input("Insira a sua altura:   "))
print(f"Peso ideal homens: {(72.7 * h) - 58:.1f}")
print(f"Peso ideal mulheres: {(62.1 * h) - 44.7:.1f}")
