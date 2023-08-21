# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

nnum = int(input("Insira a quantidade de números que deseja comparar:   "))
soma = 0
natual = None
nmaior = None
nmenor = None

for i in range(nnum):
    n = float(input(f"Insira o {i + 1}° número:   "))
    n = int(n) if n % 1 == 0 else float(n)
    soma += n

    if natual is None:
        natual = n
        nmenor = n
        nmaior = n

    # Define o menor número
    if n < natual and n < nmenor:
        nmenor = n
    elif natual < n and natual < nmenor:
        nmenor = natual

    # Define o maior número
    if n > natual and n > nmaior:
        nmaior = n
    elif natual > n and natual > nmaior:
        nmaior = natual

    natual = n


print(f"Maior = {nmaior}\nMenor = {nmenor}\nSoma dos números digitados = {soma}")
