# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
# a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva
# o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

A = 80000
B = 200000
anos = 0

while A < B:
    anos += 1
    A += A / 100 * 3
    B += B / 100 * 1.5
if A == B:
    print(f"O país A terá a mesma quantidade de habitantes que o país B em {anos}, sendo {round(A)} habitantes")
else:
    print(f"O país A excederá o tamanho da população do país B em {anos} anos, sendo A = {round(A)} e B = {round(B)}")
