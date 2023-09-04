# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as numa lista. Após isto, calcule a
# média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar
# o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temp = {
    'Janeiro': 0,
    'Fevereiro': 0,
    'Março': 0,
    'Abril': 0,
    'Maio': 0,
    'Junho': 0,
    'Julho': 0,
    'Agosto': 0,
    'Setembro': 0,
    'Outubro': 0,
    'Novembro': 0,
    'Dezembro': 0
}
mediaAcima = {}

for i in temp:
    temp[i] = float(input(f"Insira a temperatura do mês de {i}: "))

media = sum(temp.values()) / len(temp)
print(f"\nA média de temperatura deste ano foi de {media} graus")

for i in temp:
    if temp[i] > media:
        mediaAcima[i] = temp[i]

print("Meses com temperatura acima da média anual:")
for i in mediaAcima:
    print(f"{i}: {mediaAcima[i]} graus")
