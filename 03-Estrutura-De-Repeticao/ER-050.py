# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = h = 0
exp = ""

while True:
    n = int(input("Insira um número inteiro positivo: "))
    if n <= 0:
        print("Inválido!")
    else:
        break

for i in range(1, n + 1):
    h += 1/i
    if exp == "":
        exp = f"{i}"
    else:
        exp = f"{exp} + 1/{i}"

print(f"h = {exp}")
print(f"h = {h}")
