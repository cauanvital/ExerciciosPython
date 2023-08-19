# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input("Digite o primeiro número:   "))
n2 = int(input("Digite o segundo número:   "))
n3 = int(input("Digite o terceiro número:   "))

if n1 == n2 == n3:
    print("Os três números digitados são iguais")
elif n1 > n2 > n3:
    print(f"Ordem decrescente: {n1}, {n2}, {n3}")
elif n1 > n3 > n2:
    print(f"Ordem decrescente: {n1}, {n3}, {n2}")
elif n2 > n1 > n3:
    print(f"Ordem decrescente: {n2}, {n1}, {n3}")
elif n2 > n3 > n1:
    print(f"Ordem decrescente: {n2}, {n3}, {n1}")
elif n3 > n1 > n2:
    print(f"Ordem decrescente: {n3}, {n1}, {n2}")
elif n3 > n2 > n1:
    print(f"Ordem decrescente: {n3}, {n2}, {n1}")
elif n1 > n2 == n3:
    print(f"Ordem decrescente: {n1}, {n2}, {n3}")
elif n2 > n3 == n1:
    print(f"Ordem decrescente: {n2}, {n3}, {n1}")
elif n3 > n2 == n1:
    print(f"Ordem decrescente: {n3}, {n1}, {n2}")
else:
    print("Bruh")
