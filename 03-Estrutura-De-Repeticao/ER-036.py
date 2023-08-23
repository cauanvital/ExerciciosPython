# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
# não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
# usuário, conforme exemplo abaixo:
#       Montar a tabuada de: 5
#       Começar por: 4
#       Terminar em: 7
#
#       Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#       5 X 4 = 20
#       5 X 5 = 25
#       5 X 6 = 30
#       5 X 7 = 35

n = int(input("Montar a tabuada de:   "))
iniN = int(input("Começar por:   "))
fimN = int(input("Terminar por:   "))

print(f"\nVou montar a tabuada de {n} começando em {iniN} e terminando em {fimN}:")

for i in range(iniN, fimN+1 if fimN > iniN else fimN-1, -1 if iniN > fimN else 1):
    print(f"{n} X {i} = {n * i}")
