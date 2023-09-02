# O cardápio de uma lanchonete é o seguinte:
#       Especificação   Código  Preço
#       Cachorro Quente 100     R$ 1,20
#       Bauru Simples   101     R$ 1,30
#       Bauru com ovo   102     R$ 1,50
#       Hambúrguer      103     R$ 1,20
#       Cheeseburguer   104     R$ 1,30
#       Refrigerante    105     R$ 1,00
#       Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser
#       pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o
#       pedido deve ser encerrado.

preco100 = preco101 = preco102 = preco103 = preco104 = preco105 = 0
qtd100 = qtd101 = qtd102 = qtd103 = qtd104 = qtd105 = 0

while True:
    cod = int(input("Insira o código do produto: "))
    if cod != 100 and cod != 101 and cod != 102 and cod != 103 and cod != 104 and cod != 105 and cod != 0:
        print("Valor Incálido! Tente novamente")
        continue
    if cod == 0: break

    while True:
        qtdProd = int(input(f"Insira a quatidade do produto de código {cod}: "))
        if qtdProd > 0: break
        else: print("Valor Inválido! Tente novamente")

    if cod == 100:
        preco100 += qtdProd * 1.2
        qtd100 += qtdProd
    elif cod == 101:
        preco101 += qtdProd * 1.3
        qtd101 += qtdProd
    elif cod == 102:
        preco102 += qtdProd * 1.5
        qtd102 += qtdProd
    elif cod == 103:
        preco103 += qtdProd * 1.2
        qtd103 += qtdProd
    elif cod == 104:
        preco104 += qtdProd * 1.3
        qtd104 += qtdProd
    elif cod == 105:
        preco105 += qtdProd * 1.0
        qtd105 += qtdProd

valTotal = preco100 + preco101 + preco102 + preco103 + preco104 + preco105
print("\n|     Produto     | Quantidade | Valor Parcial\n"
      "| Cachorro Quente |", " " * (9 - len(str(qtd100))), f"{qtd100} | R$ {preco100:.2f}\n"
      "| Bauru Simples   |", " " * (9 - len(str(qtd101))), f"{qtd101} | R$ {preco101:.2f}\n"
      "| Bauru com ovo   |", " " * (9 - len(str(qtd102))), f"{qtd102} | R$ {preco102:.2f}\n"
      "| Hambúrguer      |", " " * (9 - len(str(qtd103))), f"{qtd103} | R$ {preco103:.2f}\n"
      "| Cheeseburguer   |", " " * (9 - len(str(qtd104))), f"{qtd104} | R$ {preco104:.2f}\n"
      "| Refrigerante    |", " " * (9 - len(str(qtd105))), f"{qtd105} | R$ {preco105:.2f}\n"
      f"\nTotal a pagar: R$ {valTotal:.2f}")
