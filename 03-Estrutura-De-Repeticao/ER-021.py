# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
# é divisível somente por ele mesmo e por 1.

n = int(input("Insira um número inteiro: "))
exit("Valor inválido! Digite um número maior que 0") if n < 1 else None
cont = 0

for i in range(1, n):
    if n % i == 0:
        cont += 1

if cont > 1 or n == 1:
    print(f"{n} não é um número primo")
else:
    print(f"{n} é um número primo")
