# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.

qtdpess = int(input("Insira a quantidade de pessoas para o cálculo:   "))
exit("Valor Inválido! Insira uma quantidade maior que 1") if qtdpess <= 1 else None
soma = 0
i = 1

while i < qtdpess + 1:
    idade = int(input(f"Insira a idade da {i}ª pessoa:   "))
    if idade <= 0:
        print("Valor Inválido! Insira uma idade maior que 0")
        continue
    soma += idade
    i += 1

media = soma / qtdpess

if 1 <= media <= 25:
    print(f"A idade média desse grupo é igual a {media}, sendo um grupo jovem")
elif 26 <= media <= 60:
    print(f"A idade média desse grupo é igual a {media}, sendo um grupo adulta")
else:
    print(f"A idade média desse grupo é igual a {media}, sendo um grupo idosa")
