# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
# em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

i = 1
soma = 0
qtdCD = int(input("Insira a quantidade de CDs da coleção:   "))

while qtdCD < 2:
    print("Coleção? Tem que ter no mínimo dois né, amigo")
    qtdCD = int(input("Insira a quantidade de CDs da coleção:   "))

while i < qtdCD + 1:
    valCD = float(input(f"Insira o valor do {i}º CD em reais:   "))

    if valCD <= 0:
        print("Valor Inválido! Insira um valor maior que zero")
        continue

    soma += valCD
    i += 1

media = soma / qtdCD
print(f"A média do valor pago em cada CD foi R${round(media, 2)}")
