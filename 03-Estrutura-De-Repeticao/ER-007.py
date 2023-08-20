# Faça um programa que leia 5 números e informe o maior número.

print(-1 > -6)
n = []
maior = 0
for i in range(5):
    n.append(int(input(f"Insira o {i + 1}º número inteiro:   ")))
    if i == 0:
        maior = n[0]
    if n[i] > maior:
        maior = n[i]

print(f"O maior valor digitado foi {maior}")
