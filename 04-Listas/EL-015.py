# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
# quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#       Mostre a quantidade de valores lidos;
#       Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#       Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#       Calcule e mostre a soma dos valores;
#       Calcule e mostre a média dos valores;
#       Calcule e mostre a quantidade de valores acima da média calculada;
#       Calcule e mostre a quantidade de valores abaixo de sete;
#       Encerre o programa com uma mensagem;

vet = []
deLadinho = ""
acimaMedia = abaixo7 = 0

while True:
    n = float(input("Insira uma nota: "))
    if n < 0: break
    vet.append(n)
print(f"\nForam lidos {len(vet)} valores")

media = sum(vet) / len(vet)
for i in vet:
    if i > media:
        acimaMedia += 1
    if i < 7:
        abaixo7 += 1

    if deLadinho == "":
        deLadinho = f"{i}"
    else:
        deLadinho = f"{deLadinho} | {i}"
print(f"\n{deLadinho}\n")

for i in vet[::-1]:
    print(i)

print(f"\nSoma dos valores: {sum(vet)}")
print(f"\nMédia dos valores: {media}")
print(f"\nQuantidade de notas acima da média: {acimaMedia}")
print(f"\nQuantidade de notas abaixo de 7: {abaixo7}")
