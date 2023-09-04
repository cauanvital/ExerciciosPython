# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#       "Telefonou para a vítima?"
#       "Esteve no local do crime?"
#       "Mora perto da vítima?"
#       "Devia para a vítima?"
#       "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa
#       no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e
#       4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

crime = {
    'Telefonou para a vítima? ': 0,
    'Esteve no local do crime? ': 0,
    'Mora perto da vítima? ': 0,
    'Devia para a vítima? ': 0,
    'Já trabalhou com a vítima? ': 0
}
culpa = 0

for i in crime:
    crime[i] = bool(int(input(f"{i}(Digite 1 para SIM e 0 para NÃO): ")))
    if crime[i] is True: culpa += 1

if culpa == 2:
    print("Classificação: suspeito")
elif culpa == 3 or culpa == 4:
    print("Classificação: cúmplice")
elif culpa == 5:
    print("Classificação: assassino")
else:
    print("Classificação: inocente")
