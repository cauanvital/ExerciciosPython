# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário.

n = int(input("Insira um número inteiro: "))

while n < 1:
    print("Valor inválido! Digite um número maior que 0")
    n = int(input("Insira um número inteiro: "))

qtdpri = 0
tamstr = 100
primos = ""

for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        qtdpri += 1
        if primos == "":
            primos = f"{i}"
        else:
            if len(primos) < tamstr:
                primos = f"{primos}, {i}"
            else:
                primos = f"{primos}\n{i}"
                tamstr += 100

primos = primos[::-1].replace(",", "e ", 1)
primos = primos[::-1]

exit(print(f"Entre 1 e {n} não existem números primos")) if qtdpri == 0 else None
exit(print(f"Entre 1 e {n} existe 1 número primo, sendo ele o número {primos}")) if qtdpri == 1 else None
print(f"Entre 1 e {n} existem {qtdpri} números primos, sendo eles:\n{primos}")
