# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.

con = 1

while con == 1:
    n = int(input("Insira um número inteiro:   "))
    if n > 15 or n < 0:
        print("Valor Inválido! Insira um valor de 0 a 16")
        continue
    res = n
    f = ""

    if n == 1 or n == 0:
        print(f"{n}! = 1")
        continue

    for i in range(1, n):
        res *= i
        f = f". {i} {f}"

    f = f"{n} {f}"
    print(f"{n}! = {f} = {res}")

    con = int(input("Quer tentar de novo? Digite 1 para sim e 0 para não:   "))
    while con != 0 and con != 1:
        print("Opção Inválida! Digite 1 para sim e 0 para não")
        con = int(input("Quer tentar de novo? Digite 1 para sim e 0 para não:   "))

print("Tenha um bom dia!")
