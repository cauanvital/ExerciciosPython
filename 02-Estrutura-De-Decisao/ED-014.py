# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
# a sua média. A atribuição de conceitos obedece à tabela abaixo:
#       Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0        A
#       Entre 7.5 e 9.0         B
#       Entre 6.0 e 7.5         C
#       Entre 4.0 e 6.0         D
#       Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
# for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Insira a primeira nota:   "))
n2 = float(input("Insira a segunda nota:   "))
media = (n1 + n2) / 2
resul = None
conce = None

if 9.0 <= media:
    conce = "A"
    resul = "APROVADO"
elif 7.5 <= media:
    conce = "B"
    resul = "APROVADO"
elif 6.0 <= media:
    conce = "C"
    resul = "APROVADO"
elif 4.0 <= media:
    conce = "D"
    resul = "REPROVADO"
else:
    conce = "E"
    resul = "REPROVADO"

print(f"A média entre {n1} e {n2} é igual a {media}")
print(f"Conceito: {conce}")
print(f"Resultado: {resul}")
