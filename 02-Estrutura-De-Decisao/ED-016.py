# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
# os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#       Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
#       pedir osdemais valores, sendo encerrado;
#       Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#       Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#       Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;

a = float(input("Digite o valor de A:   "))

if a == 0:
    exit("\"0\" não é um valor válido")

b = float(input("Digite o valor de B:   "))
c = float(input("Digite o valor de C:   "))
delta = pow(b, 2) + (-4 * a * c)

print(delta)

if delta < 0:
    print("Esta equação possui o delta menor que zero e não possui solução real")
elif delta > 0:
    resu1 = (-b + pow(delta, 1/2)) / (2 * a)
    resu2 = (-b - pow(delta, 1/2)) / (2 * a)
    print(f"A equação possui 2 resultados possiveis, sendo eles {resu1} e {resu2}")
else:
    resu = -b / (2 * a)
    print(f"A equação possui 1 resultado possivel, sendo ele {resu}")
