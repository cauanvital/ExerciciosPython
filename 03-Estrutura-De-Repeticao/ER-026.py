# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
# votar e ao final mostrar o número de votos de cada candidato.

qtdelei = int(input("Insira a quantidade de eleitores:   "))
exit("Valor Inválido! Insira um valor maior que 1") if qtdelei <= 1 else None
i = 1
rogevot = 0
victvot = 0
morgvot = 0

print("Para votar em Rogerinho do Ingá, digite 1")
print("Para votar em Victor Schiavon, digite 2")
print("Pada votar em Morgan Freeman, digite 3")

while i < qtdelei + 1:
    voto = int(input(f"{i}º voto:   "))

    if voto != 1 and voto != 2 and voto != 3:
        print("Escolha um candidato válido")
        continue

    if voto == 1:
        rogevot += 1
    elif voto == 2:
        victvot += 1
    else:
        morgvot += 1

    i += 1

perroge = round(rogevot * 100 / qtdelei, 1)
pervict = round(victvot * 100 / qtdelei, 1)
permorg = round(morgvot * 100 / qtdelei, 1)

print(f"Rogerinho do Ingá teve {rogevot} votos, sendo {perroge}% dos eleitores totais")
print(f"Victor Schiavon teve {victvot} votos, sendo {pervict}% dos eleitores totais")
print(f"Morgan Freeman teve {morgvot} votos, sendo {permorg}% dos eleitores totais")

if rogevot > morgvot and rogevot > victvot:
    print("Rogerinho do Ingá foi eleito")
elif victvot > rogevot and victvot > morgvot:
    print("Victor Schiavon foi eleito")
elif morgvot > rogevot and morgvot > victvot:
    print("Morgan Freeman foi eleito")
else:
    print("Parece que precisaremos de um segundo turno...")
