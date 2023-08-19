# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = str(input("Digite uma data no seguinte formato \"dd/mm/aaaa\":   "))

if len(data) != 10:
    exit("Formato Inválido! Tem que ter exatamente 10 caracteres.")
elif data[2] != "/" and data[5] != "/":
    exit("Formato Inválido! As \"/\" não foram inseridas da forma correta.")
elif not data[0:2].isnumeric() or not data[3:5].isnumeric() or not data[6:].isnumeric():
    exit("Formato Inválido! Os números não foram inseridos de forma correta.")

if 1 < int(data[3:5]) > 12:
    exit("Mês Inválido")
elif 1 < int(data[0:2]) > 31:
    exit("Dia Inválido")
else:
    print("Data Válida")
