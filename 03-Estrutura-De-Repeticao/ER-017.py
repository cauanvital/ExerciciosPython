# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input("Insira um número inteiro:   "))
exit("Número Inválido! O número deve ser maior ou igual a zero.") if n < 0 else None
res = n
f = ""

if n == 1 or n == 0:
    print(f"{n}! = 1")
    exit()

for i in range(1, n):
    res *= i
    f = f". {i} {f}"

f = f"{n} {f}"
print(f"{n}! = {f} = {res}")
