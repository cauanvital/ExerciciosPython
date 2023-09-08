# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
# pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
# pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado
# quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#
#       Atleta: Rodrigo Curvêllo
#
#       Primeiro Salto: 6.5 m
#       Segundo Salto: 6.1 m
#       Terceiro Salto: 6.2 m
#       Quarto Salto: 5.4 m
#       Quinto Salto: 5.3 m
#
#       Resultado final:
#       Atleta: Rodrigo Curvêllo
#       Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#       Média dos saltos: 5.9 m

while True:
    stringSaltos = ""
    ordinal = {0: "Primeiro", 1: "Segundo", 2: "Terceiro", 3: "Quarto", 4: "Quinto"}
    saltos = []
    atleta = str(input("\nAtleta: "))
    if atleta == "":
        break

    print()

    for i in ordinal.values():
        j = float(input(f"{i} salto: "))

        if not saltos:
            stringSaltos = f"{j}"
        else:
            stringSaltos = f"{stringSaltos} - {j}"

        saltos.append(j)

    print("\nResultado final:"
          f"\nAtleta: {atleta}"
          f"\nSaltos: {stringSaltos}"
          f"\nMédia dos saltos: {sum(saltos) / len(saltos)}")

print("\nTenha um bom dia!")
