# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [0, 0, 0, 0]

for i in range(4):
    notas[i] = float(input("Insira uma nota: "))

media = sum(notas) / len(notas)
print(f"Notas: {notas}")
print(f"Média: {media:.1f}")
