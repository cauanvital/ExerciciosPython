# Faça um programa que leia e valide as seguintes informações:
#       Nome: maior que 3 caracteres;
#       Idade: entre 0 e 150;
#       Salário: maior que zero;
#       Sexo: 'f' ou 'm';
#       Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Nome:   "))
while len(nome) < 4:
    print("Nome inválido! Tente novamente")
    nome = str(input("Nome:   "))

idade = int(input("Idade:   "))
while idade < 1 or idade > 150:
    print("Idade inválida! Tente novamente")
    idade = int(input("Idade:   "))

salario = float(input("Salário:   "))
while salario <= 0:
    print("Salário inválida! Tente novamente")
    salario = float(input("Salário:   "))

sexo = str(input("Sexo:   ")).upper()
while sexo != "M" and sexo != "F":
    print("Sexo inválido! Tente novamente")
    sexo = str(input("Sexo:   ")).upper()

estcivil = str(input("Estado Civil:   ")).upper()
while estcivil != "S" and estcivil != "C" and estcivil != "V" and estcivil != "D":
    print("Estado Civil inválido! Tente novamente")
    estcivil = str(input("Estado Civil:   ")).upper()

print("Tudo certo!")
