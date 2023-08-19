# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
# ele mostre os números um ao lado do outro.

for i in range(20):
    i += 1
    print(i)

r = ""
for i in range(20):
    i += 1
    r = f"{r} {i}"

print(r)
