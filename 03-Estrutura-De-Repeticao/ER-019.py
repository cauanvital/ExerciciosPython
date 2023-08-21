# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

nnum = int(input("Insira a quantidade de números que deseja comparar:   "))
soma = 0
i = 0
natual = None
nmaior = None
nmenor = None

while i < nnum:
    i += 1
    n = float(input(f"Insira o {i}° número:   "))
    n = int(n) if n % 1 == 0 else float(n)
    if n < 0 or n > 1000:
        print("Número Inválido! Tente um número entre 0 e 1000")
        i -= 1
        continue
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


print(f"\nMaior = {nmaior}\nMenor = {nmenor}\nSoma dos números digitados = {soma}")
