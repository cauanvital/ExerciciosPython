# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
# entrada e permita repetir a operação.

conti = "N"

while conti == "N":
    popA = float(input("Insira a população do país A:   "))
    taxA = float(input("Insira a taxa que crescimento anual da população do país A:   "))
    popB = float(input("Insira a população do país B:   "))
    taxB = float(input("Insira a taxa que crescimento anual da população do país B:   "))
    menor = min(popA, popB)
    maior = max(popA, popB)
    anos = 0

    while menor < maior:
        anos += 1
        popA += popA / 100 * taxA
        popB += popB / 100 * taxB

    if popA == popB:
        print(f"O país A terá a mesma quantidade de habitantes que o país B em {anos}, "
              f"sendo {round(popA)} habitantes")
    else:
        if popA > popB:
            print(f"O país A irá ultrapassar a população do país B em {anos} anos, "
                  f"sendo A = {round(popA)} e B = {round(popB)}")
        else:
            print(f"O país B irá ultrapassar a população do país A em {anos} anos, "
                  f"sendo B = {round(popB)} e A = {round(popA)}")
