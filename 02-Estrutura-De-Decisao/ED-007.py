# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite o primeiro número:   "))
n2 = int(input("Digite o segundo número:   "))
n3 = int(input("Digite o terceiro número:   "))

menor = min(n1, n2, n3)
maior = max(n1, n2, n3)

if n1 == n2 == n3:
    print("Os número digitados são iguais")
else:
    print(f"O maior valor digitado foi {maior} e o menor foi {menor}")
