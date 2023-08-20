# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for i in range(5):
    n = float(input(f"Insira o {i + 1}º número:   "))
    soma += n

media = soma / 5
print(f"A soma dos números digitados é {soma} e a média entre eles é {media}")
