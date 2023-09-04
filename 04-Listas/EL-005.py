# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
# números IMPARES no vetor impar. Imprima os três vetores.

n = []
impar = []
par = []

for i in range(20):
    n.append(int(input(f"Insira o {i + 1}º número: ")))
    print(n)
    if n[i] % 2 == 0:
        par.append(n[i])
    else:
        impar.append(n[i])

print(f"\nTodos os números inseridos: {n}")
print(f"Números ímpares: {impar}")
print(f"Números pares: {par}")
