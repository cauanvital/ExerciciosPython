# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    n[i] = int(input("Insira um número inteiro: "))
print(n[::-1])
