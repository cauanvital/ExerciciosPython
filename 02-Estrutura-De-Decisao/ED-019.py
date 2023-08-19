# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
# do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

n = int(input("Insira um número inteiro de 1 a 999:   "))
u = n % 10
d = int(((n - u) / 10) % 10)
c = int(((n - d * 10) - u) / 100)

uq = f"{u} unidade" if u == 1 else f"{u} unidades"
dq = f"{d} dezena" if d == 1 else f"{d} dezenas"
cq = f"{c} centena" if c == 1 else f"{c} centenas"

if 1000 < n or n <= 0:
    exit("Número inválido! Insira um número inteiro entre 1 e 999.")

elif c == 0 and d == 0 and u != 0:
    print(f"{n} = {uq}")
elif c == 0 and d != 0 and u == 0:
    print(f"{n} = {dq}")
elif c != 0 and d == 0 and u == 0:
    print(f"{n} = {cq}")

elif c != 0 and d == 0 and u != 0:
    print(f"{n} = {cq} e {uq}")
elif c != 0 and d != 0 and u == 0:
    print(f"{n} = {cq} e {dq}")
elif c == 0 and d != 0 and u != 0:
    print(f"{n} = {dq} e {uq}")

else:
    print(f"{n} = {cq}, {dq} e {uq}")
