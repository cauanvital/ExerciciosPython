# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi

raio = float(input("Insira o raio do circulo em centímetros:   "))
area = pi * pow(raio, 2)
print(f"A área do círculo é igual a {area:.2f}cm2")
