# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador
# módulo(resto da divisão).

n = int(input("Insira um número inteiro:    "))

if n % 2 != 0:
    print(f"{n} é um número ímpar")
else:
    print(f"{n} é um número par")
