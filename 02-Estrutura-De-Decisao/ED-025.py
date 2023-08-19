# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#       "Telefonou para a vítima?"
#       "Esteve no local do crime?"
#       "Mora perto da vítima?"
#       "Devia para a vítima?"
#       "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa
#       no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3
#       e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Você está sendo questionado sobre um crime. Responde \"S\" para SIM e \"N\" para NÃO.")
r1 = str(input("Telefonou para a vítima?   ")).upper()
exit("Resposta Inválida") if r1 != "S" and r1 != "N" else None
r2 = str(input("Esteve no local do crime?   ")).upper()
exit("Resposta Inválida") if r2 != "S" and r2 != "N" else None
r3 = str(input("Mora perto da vítima?   ")).upper()
exit("Resposta Inválida") if r3 != "S" and r3 != "N" else None
r4 = str(input("Devia para a vítima?   ")).upper()
exit("Resposta Inválida") if r4 != "S" and r4 != "N" else None
r5 = str(input("Já trabalhou com a vítima?   ")).upper()
exit("Resposta Inválida") if r5 != "S" and r5 != "N" else None
estatis = [r1, r2, r3, r4, r5].count("S")

if estatis < 2:
    print("Inocente... por enquanto.")
elif estatis == 2:
    print("Suspeito")
elif 2 < estatis < 5:
    print("Cúmplice")
else:
    print("Culpado")
