# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série
# até o n−ésimo termo.

n = int(input("Insira um número inteiro:   "))
a = 0
b = 1
c = 0
d = ""

while c < n:
    c = a + b
    a = b
    b = c
    if c > n:
        break
    d = f"{d}{c}" if c == 1 else f"{d}, {c}"

print(f"Até o número {n} existem os seguintes números na série de Fibonacci:\n{d}")
