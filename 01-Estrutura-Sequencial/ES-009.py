# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

f = float(input("Insira a temperatura em Fahrenheit:   "))
c = 5 * ((f-32) / 9)
print(f"{f:.1f}°F equivale a {c:.1f}°C")
