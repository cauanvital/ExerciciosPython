# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro
#   Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
# gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

print("Escolha o tipo de combustível que quer abastecer, sendo \"A\" para álcool e \"G\" para gasolina.")

tipo = str(input("Insira o tipo de combustível:   ")).upper()
exit("Tipo Inválido") if tipo != "G" and tipo != "A" else None

qtd = float(input("Insira a quantidade em litros de combustível:   "))
print("De graça! Você não paga nada por nada") if qtd == 0 else None
qtd = round(qtd) if qtd % 1 == 0 else round(qtd, 1)
plural = "litro" if qtd == 1 else "litros"

valor = 2.5 * qtd if tipo == "G" else 1.9 * qtd
msg = f"Comprando {qtd} {plural} de {'gasolina' if tipo == 'G' else 'álcool'} você deverá pagar "

if qtd > 20:
    if tipo == "G":
        msg += f"R${round(valor - (0.15 * qtd), 2):.2f} com 6% de desconto por litro"
    else:
        msg += f"R${round(valor - (0.095 * qtd) + 0.05, 2):.2f} com 5% de desconto por litro"
else:
    if tipo == "G":
        msg += f"R${round(valor - (0.1 * qtd), 2):.2f} com 4% de desconto por litro"
    else:
        msg += f"R${round(valor - (0.057 * qtd) + 0.05, 2):.2f} com 3% de desconto por litro"

print(msg)
