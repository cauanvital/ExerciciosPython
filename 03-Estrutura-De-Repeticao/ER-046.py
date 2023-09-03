# Numa competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
# atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
# informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a
# média). Use uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não
# são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser
# conforme o exemplo abaixo:
#
#       Atleta: Rodrigo Curvêllo
#
#       Primeiro Salto: 6.5 m
#       Segundo Salto: 6.1 m
#       Terceiro Salto: 6.2 m
#       Quarto Salto: 5.4 m
#       Quinto Salto: 5.3 m
#
#       Melhor salto:  6.5 m
#       Pior salto: 5.3 m
#       Média dos demais saltos: 5.9 m
#
#       Resultado final:
#       Rodrigo Curvêllo: 5.9 m

from statistics import median

saltos = [0, 0, 0, 0, 0]
nomVencedor = resVencedor = None


while True:
    i = 0
    nomeAtleta = str(input("Insira o nome do atleta: "))

    if nomeAtleta == "":
        break

    while i < 5:
        saltos[i] = float(input(f"Insira o {i + 1}º salto: "))
        if saltos[i] < 0:
            print("Insira um valor positivo!")
            continue
        i += 1

    if nomVencedor is None:
        nomVencedor = nomeAtleta
        resVencedor = median(saltos)
    elif median(saltos) > resVencedor:
        nomVencedor = nomeAtleta
        resVencedor = median(saltos)

    print(f"\nAtleta: {nomeAtleta}"
          f"\nPrimeiro Salto: {saltos[0]:.1f} m"
          f"\nSegundo Salto: {saltos[1]:.1f} m"
          f"\nTerceiro Salto: {saltos[2]:.1f} m"
          f"\nQuarto Salto: {saltos[3]:.1f} m"
          f"\nQuinto Salto: {saltos[4]:.1f} m\n"
          f"\nMelhor Salto: {max(saltos):.1f} m"
          f"\nPior Salto: {min(saltos):.1f} m"
          f"\nMédia dos Demais Saltos: {median(saltos):.1f} m\n")

print(f"\nVencedor: {nomVencedor}"
      f"\nMédia do Vencedor: {resVencedor} m")
