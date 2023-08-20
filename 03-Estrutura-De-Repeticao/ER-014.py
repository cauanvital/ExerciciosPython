# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
# números impares.

imp = 0
par = 0

for i in range(1, 11):
    n = int(input(f"Insira o {i}° número inteiro:   "))
    if n % 2 == 0:
        par += 1
    else:
        imp += 1

if imp == 0:
    print(f"Dentre os números digitados existem {par} números pares")
elif par == 0:
    print(f"Dentre os números digitados existem {imp} números ímpares")
else:
    print(f"Dentre os números digitados existem {par} números pares e {imp} números ímpares")
