# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("M - Matutino\nV - Vespertino\nN - Noturno")
turn = str(input("Em qual turno você estuda?   ")).upper()

if turn == "M":
    print("Bom Dia!")
elif turn == "V":
    print("Boa Tarde!")
elif turn == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
