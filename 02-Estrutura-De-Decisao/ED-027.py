# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                             Até 5 Kg           Acima de 5 Kg
#       Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#       Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# P.S.: Troquei maçã por tomate porque eu sou maluco

morang = float(input("Insita a quantidade em quilos de morango que deseja comprar:   "))
tomate = float(input("Insita a quantidade em quilos de tomate que deseja comprar:   "))
valtoma = tomate * 1.5 if tomate > 5 else tomate * 1.8
valmora = morang * 2.2 if morang > 5 else morang * 2.5
valtota = valmora + valtoma
qtdtota = None

if morang + tomate > 8 or valtoma + valmora > 25:
    valtota -= valtota / 100 * 10

if morang == 0:
    qtdtota = f"{tomate:.3f}kg de tomate"
elif tomate == 0:
    qtdtota = f"{morang:.3f}kg de morango"
else:
    qtdtota = f"{morang:.3f}kg de morango e {tomate:.3f}kg de tomate"
print(f"Comprando {qtdtota} você deverá pagar R${valtota:.2f}")
