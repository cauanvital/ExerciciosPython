# Os números primos possuem várias aplicações na Computação, por exemplo, na Criptografia. Um número primo é aquele
# que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou
# não um número primo.

n = int(input("Insira um número inteiro positivo:   "))
div = 0
exit(print(f"{n} não é um número primo.")) if n <= 1 else None

while n < 0:
    print("Número inválido! Tente novamente.")
    n = int(input("Insira um número inteiro positivo:   "))

for i in range(1, n):
    if n % i == 0:
        div += 1

    if div > 1:
        print(f"{n} não é um número primo.")
        exit()

print(f"{n} é um número primo.")
