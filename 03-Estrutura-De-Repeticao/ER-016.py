# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que
# o valor seja maior que 500.

a = 0
b = 1
c = 0
d = "0 1"

while c < 500:
    c = a + b
    a = b
    b = c
    if c > 500:
        break
    d = f"{d} {c}"

print(d)
