# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
# número. Não utilize a função de potência da linguagem.

n1 = float(input("Insira o número base da potenciação:   "))
n2 = int(input("Insira o número expoente da potenciação:   "))
res = 1

for i in range(n2):
    res *= n1

print(f"{n1} elevado a {n2} é igual a {res}")
