# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#       o produto do dobro do primeiro com metade do segundo .
#       a soma do triplo do primeiro com o terceiro.
#       o terceiro elevado ao cubo.

numi1 = int(input("Digite um número inteiro:   "))
numi2 = int(input("Digite outro número inteiro:   "))
numr = float(input("Digite um número real:   "))
print(f"O produto entre o dobro de {numi1} e a metade de {numi2} é {(numi1 * 2) * (numi2 / 2)}")
print(f"A soma do triplo de {numi1} com {numr} é {numi1 * 3 + numr}")
print(f"{numr} elevado ao cubo é igual a {pow(numr, 3)}")
