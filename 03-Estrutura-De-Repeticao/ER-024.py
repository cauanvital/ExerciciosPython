# Faça um programa que calcule o mostre a média aritmética de N notas.

qtdnota = int(input("Insira a quantidade de notas que deseja calcular a média:   "))
exit("Valor Inválido! Insira uma quantidade maior que 1") if qtdnota <= 1 else None
soma = 0

for i in range(1, qtdnota + 1):
    nota = float(input(f"Insira o valor da {i}ª nota:   "))
    soma += nota

media = soma / qtdnota

print(f"A média aritmética das notas inseridas é igual a {media}")
