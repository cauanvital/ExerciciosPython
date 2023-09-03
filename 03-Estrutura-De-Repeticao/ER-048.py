# Faça um programa que peça um número inteiro positivo e em seguida mostre este numero invertido.
#       Exemplo:
#           12376489
#           => 98467321

n = 0
div1 = div2 = 1
inverse = ""

while True:
    n = int(input("Insira um número inteiro positivo: "))
    if n < 0:
        print("Inválido!")
    else:
        break

for i in range(len(str(n))):
    div1 = int(f"{div1}0")
    u = (n % div1) // div2
    inverse = f"{inverse}{u}"
    div2 = int(f"{div2}0")

print(f"=> {inverse}")
