# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número
# ele é divisível.

n = int(input("Insira um número inteiro: "))
exit("Valor inválido! Digite um número maior que 0") if n < 1 else None
cont = 0
div = ""

for i in range(2, n):
    if n % i == 0:
        cont += 1
        if i == 1:
            div = "1"
        else:
            div = f"{div}, {i}"

if cont > 0:
    print(f"{n} não é um número primo, sendo divisivel por {div} e {n}")
elif n == 1:
    print("1 não é um número primo pois possui apenas um divisor")
else:
    print(f"{n} é um número primo, sendo divisivel apenas por 1 e {n}")
