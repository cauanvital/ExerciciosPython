# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
# mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
# existentes na máquina.
#       Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota
#       de 5 e uma nota de 1;
#       Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro
#       notas de 10, uma nota de 5 e quatro notas de 1.

val = float(input("Isira a quantia que quer sacar entre R$10,00 e R$600,00:   "))
qcem = int(val // 100)
qciq = int(val % 100 // 50)
qdez = int(val % 100 % 50 // 10)
qcin = int(val % 100 % 50 % 10 // 5)
qtum = int(val % 100 % 50 % 10 % 5)

qcemq = f"{qcem} nota de cem" if qcem == 1 else f"{qcem} notas de cem"
qciqq = f"{qciq} nota de cinquenta" if qciq == 1 else f"{qciq} notas de cinquenta"
qdezq = f"{qdez} nota de dez" if qdez == 1 else f"{qdez} notas de dez"
qcinq = f"{qcin} nota de cinco" if qcin == 1 else f"{qcin} notas de cinco"
qtumq = f"{qtum} nota de um" if qtum == 1 else f"{qtum} notas de um"

if val > 600 or val < 10:
    exit("Valor Inválido!")

print(f"Para sacar R${val:.2f}, o programa fornece: ")

if qcem != 0:
    print(f"    {qcemq}")
if qciq != 0:
    print(f"    {qciqq}")
if qdez != 0:
    print(f"    {qdezq}")
if qcin != 0:
    print(f"    {qcinq}")
if qtum != 0:
    print(f"    {qtumq}")
