# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

n = 13

while 0 < n or n > 10:
    n = int(input("Digite uma nota entre 0 e 10:   "))
    if 0 < n > 10:
        print("Valor inválido! Tente novamente")
    else:
        print("Valor válido! Muito obrigado")
        break
