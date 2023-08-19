# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input("Insira a temperatura em Celsius:   "))
f = 32 + (c * 9/5)
print(f"{c:.1f}°C equivale a {f:.1f}°F")
