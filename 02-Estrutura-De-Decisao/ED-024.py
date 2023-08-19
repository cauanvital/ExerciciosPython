# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#       par ou ímpar;
#       positivo ou negativo;
#       inteiro ou decimal.

n1 = float(input("Insira o primeiro número:   "))
n2 = float(input("Insira o segundo número:   "))
op = str(input("Insira a operção que deseja realizar:   "))
res = None
info = None

n1 = round(n1) if n1 % 1 == 0 else n1
n2 = round(n2) if n2 % 1 == 0 else n2

if op != "*" and op != "/" and op != "+" and op != "-":
    exit("Operação Inválida! São apenas permitidos \"*\" (multiplicação),\"/\" (divisão),"
         " \"-\" (subtração) e \"+\" (adição)")

if op == "*":
    res = n1 * n2
elif op == "/":
    res = n1 / n2
elif op == "+":
    res = n1 + n2
else:
    res = n1 - n2

print(f"O resultado da operação \"{n1} {op} {n2}\" é igual a {res}")

if res % 2 == 0:
    info = f"{res} é um número par, "
else:
    info = f"{res} é um número ímpar, "

if res < 0:
    info += "ngativo e "
elif res > 0:
    info += "positivo e "
else:
    info += "neutro e "

if res % 1 == 0:
    info += "inteiro"
else:
    info += "decimal"

print(info)
