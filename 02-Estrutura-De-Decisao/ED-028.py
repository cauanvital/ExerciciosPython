# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                             Até 5 Kg           Acima de 5 Kg
#       File Duplo      R$ 4,90 por kg          R$ 5,80 por kg
#       Alcatra         R$ 5,90 por kg          R$ 6,80 por kg
#       Picanha         R$ 6,90 por kg          R$ 7,80 por kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
# pagamento, valor do desconto e valor a pagar.

print("===================================================")
print("-=-=-=-= SUPER PROMOÇÂO DE CARNES TABAJARA =-=-=-=-")
print("===================================================")
print("-=-=-=-=-=-=-=-= Digite 1 para filé duplo +=-=-=-=-")
print("-=-=-=-=-=-=-=-= Digite 2 para alcatra =-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-= Digite 3 para picanha =-=-=-=-=-=-")

opcoes = {1: 'Filé duplo', 2: 'Alcatra', 3: 'Picanha'}
opcao = int(input("-=-=-=-= Escolha:   "))
if 3 < opcao or opcao < 1: exit("Opção Inválida")
qtd = float(input("-=-=-=-= Insira a quantidade em quilos:   "))
if qtd <= 0: exit("Quantidade Inválida")
forma = str(input("-=-=-=-= Pagar com cartão Tabajara? S/N   ")).upper()
if forma != "S" and forma != "N": exit("Opção Inválida")
valtota = None
descont = 0

if qtd <= 5:
    if opcao == 1:
        valtota = 4.9 * qtd
    elif opcao == 2:
        valtota = 5.9 * qtd
    else:
        valtota = 6.9 * qtd
else:
    if opcao == 1:
        valtota = 5.8 * qtd
    elif opcao == 2:
        valtota = 6.8 * qtd
    else:
        valtota = 7.8 * qtd

if forma == "S":
    descont = valtota / 100 * 5

print("\n=====================================")
print(f"======== {opcoes[opcao]} {qtd:.3f}kg")
print(f"======== Valor Total: R${valtota:.2f}")
print(f"======== Cartão Tabajara: {forma}")
print(f"======== Desconto Total: R${descont:.2f}")
print(f"======== Valor à pagar: R${valtota - descont:.2f}")
print("=====================================")
