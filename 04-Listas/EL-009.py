# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
# elementos do vetor.

a = []
b = 0

for i in range(10):
    a.append(int(input(f"{i + 1}º número: ")))
    b += a[i] * a[i]

print(f"\nA soma dos quadrados do vetor {a} é igual a {b}")
