# O Sr. Manoel Gomes expandiu os seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
# de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final
# da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para
# registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#       Lojas Tabajara
#       Produto 1: R$ 2.20
#       Produto 2: R$ 5.80
#       Produto 3: R$ 0
#       Total: R$ 9.00
#       Dinheiro: R$ 20.00
#       Troco: R$ 11.00
#       ...


j = 1

print("Lojas Tabajara")

while j != "0":
    troco = 0
    total = 0
    i = 1

    while i != 0:
        prod = float(input(f"Produto {i}: R$ "))

        if prod == 0:
            break
        total += prod
        i += 1

    print(f"Total: R$ {round(total, 2):.2f}")

    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total

    while dinheiro < total:
        if dinheiro < 0:
            print("Está tentando roubar? Insira um valor válido")
            dinheiro = float(input("Dinheiro: R$ "))
        else:
            print("Faltou dinheiro! Insira um valor maior que o total")
            dinheiro = float(input("Dinheiro: R$ "))

    print(f"Troco: R$ {round(troco, 2):.2f}")

    print("Insira \"0\" para encerrar o programa ou qualquer outro caractere para prosseguir")
    j = str(input())
