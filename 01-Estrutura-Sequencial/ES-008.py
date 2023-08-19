# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valh = float(input("Insira quanto você ganha por hora:   "))
hmes = float(input("Insira quantas você trabalhou no mês:   "))
sal = valh * hmes
print(f"Seu salário no último mês foi de R${sal:.2f}")
