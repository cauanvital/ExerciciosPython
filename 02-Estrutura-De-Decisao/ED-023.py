# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
# arredondamento.

n = float(input("Insira um número:   "))

if n % 1 == 0:
    print(f"{n:.0f} é um número inteiro")
else:
    print(f"{n} é um número decimal")

# if n.is_integer():
#     print(f"{round(n)} é um número inteiro")
# else:
#     print(f"{n} é um número decimal")

# nstr = str(n)
# if nstr.split(".")[1] == "0":
#     print(f"{round(n)} é um número inteiro")
# else:
#     print(f"{n} é um número decimal")
