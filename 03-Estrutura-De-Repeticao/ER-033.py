# O Departamento Estadual de Meteorologia contratou-lhe para desenvolver um programa que leia um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperatura informada, bem como a média
# das temperaturas.

temp = ""
tmaior = None
tmenor = None
tatual = None
soma = 0
qtdt = 0

while temp != "F":
    temp = str(input("Insira uma temperatura. Digite \"F\" para finalizar:   "))

    if temp.replace("-", "", 1).replace(".", "", 1).isnumeric():
        temp = float(temp)
        qtdt += 1
        soma += temp
    elif temp.upper() == "F":
        break
    else:
        print("Entrada inválida!")
        continue

    if tatual is None:
        tatual = temp
        tmenor = temp
        tmaior = temp

    if temp < tatual and temp < tmenor:
        tmenor = temp
    elif tatual < temp and tatual < tmenor:
        tmenor = tatual

    if temp > tatual and temp > tmaior:
        tmaior = temp
    elif tatual > temp and tatual > tmaior:
        tmaior = tatual

    tatual = temp

media = soma / qtdt
print(f"A maior temperatura registrada foi {round(tmaior, 1)} e a menor foi {round(tmenor, 1)}, sendo a média entre "
      f"todas {round(media, 1)}")
