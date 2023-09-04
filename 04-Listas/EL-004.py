# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = ["", "", "", "", "", "", "", "", "", ""]
consoantes = []

for i in range(len(letras)):
    while True:
        letras[i] = str(input(f"Insira {i + 1}º caractere: "))
        if len(letras[i]) != 1:
            print("Inválido!")
        else:
            break

    if letras[i] in "bcçdfghjklmnpqrstvxywzBCÇDFGJKLMNPQRSTVWXZ":
        consoantes.append(letras[i])

print(f"\nConsoantes: {consoantes}")
print(f"Quantidade de consoantes: {len(consoantes)}")
