# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
# compreendido por eles.

n1 = int(input("Insira um número inteiro:   "))
n2 = int(input("Insira outro número inteiro:   "))
exit(print("Os números digitados são iguais")) if n1 == n2 else None
menor = min(n1, n2)
maior = max(n1, n2)
x = ""

if menor + 2 == maior and menor + 2 == maior:
    print(f"Entre os números {menor} e {maior} existe o número {menor + 1}")
    exit()
elif menor + 1 == maior:
    print(f"Não existe nenhum número inteiro entre {menor} e {maior}")
    exit()

while menor < maior:
    menor += 1
    if menor < maior - 2:
        x = f"{x}{menor}, "
    elif menor == maior - 1:
        x = f"{x}{menor - 1}"
        x = f"{x} e {menor}"

print(f"Entre os números {n1} e {n2} existem os números {x}")
