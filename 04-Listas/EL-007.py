# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

soma = 0
multi = 1
n = []

for i in range(5):
    n.append(int(input(f"Insira o {i + 1}º número: ")))
    soma += n[i]
    multi *= n[i]

print(f"Números inseridos: {n}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multi}")
