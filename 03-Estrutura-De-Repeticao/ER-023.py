# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
# deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o
# funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Insira um número inteiro: "))
exit("Valor inválido! Digite um número maior que 0") if n < 1 else None
div = 0
qtdpri = 0
tamstr = 100
primos = ""

for i in range(2, n + 1):
    div += 1
    for j in range(2, i):
        div += 1
        if i % j == 0:
            break
    else:
        qtdpri += 1
        if primos == "":
            primos = f"{i}"
        else:
            if len(primos) < tamstr:
                primos = f"{primos}, {i}"
            else:
                primos = f"{primos}\n{i}"
                tamstr += 100

print(f"Entre 1 e {n} existem {qtdpri} números primos, sendo eles:\n{primos}")
print(f"Número de testes realizados para chegar a esses resultados: {div}")
