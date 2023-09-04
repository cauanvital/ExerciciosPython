# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima
# a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(5):
    idade.append(int(input("\nInsira a idade: ")))
    altura.append(int(input("Insira a altura: ")))

for i in range(4, -1, -1):
    print(f"\nIdade: {idade[i]}")
    print(f"Altura: {altura[i]}")
