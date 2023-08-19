# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.

val1 = float(input("Digite o valor do primeiro produto:   "))
val2 = float(input("Digite o valor do segundo produto:   "))
val3 = float(input("Digite o valor do terceiro produto:   "))
menor = min(val1, val2, val3)

if val1 == val2 == val3:
    print("Todos os valores inseridos são iguais")
else:
    print(f"O produto que custa R${menor} é o mais barato")
