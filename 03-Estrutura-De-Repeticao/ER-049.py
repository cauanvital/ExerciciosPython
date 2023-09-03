# Faça um programa que mostre os n termos da Série a seguir:
#       S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#       Imprima no final a soma da série.

n = s = 0
exp = ""
j = 1

while True:
    n = int(input("Insira um número inteiro positivo: "))
    if n < 0:
        print("Inválido!")
    else:
        break

for i in range(1, n + 1):
    s += i/j
    if exp == "":
        exp = f"{i}/{j}"
    else:
        exp = f"{exp} + {i}/{j}"
    j += 2

print(f"S = {exp}")
print(f"S = {s}")
