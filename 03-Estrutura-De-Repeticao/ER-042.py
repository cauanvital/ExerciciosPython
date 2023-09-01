# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
# seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido
# um número negativo.

count0to25 = count26to50 = count51to75 = count76to100 = 0

while True:
    n = str(input("Insira um número inteiro (digite \"F\" para finalizar): "))

    if n == "F" or n == "f":
        print("Tenha um bom dia!")
        break

    try:
        float(n)
    except ValueError:
        print("Você não digitou um número e nem \"F\"! Tente novamente.")
        continue
    else:
        n = float(n)

    if n < 0:
        print("Número negativo inserido! Tente outro.")
        continue

    if 0 <= n <= 25:
        count0to25 += 1
    elif 26 <= n <= 50:
        count26to50 += 1
    elif 51 <= n <= 75:
        count51to75 += 1
    elif 76 <= n <= 100:
        count76to100 += 1

print(f"Quantidade de números inseridos entre 0 e 25: {count0to25}\n"
      f"Quantidade de números inseridos entre 26 e 50: {count26to50}\n"
      f"Quantidade de números inseridos entre 51 e 75: {count51to75}\n"
      f"Quantidade de números inseridos entre 76 e 100: {count76to100}")
