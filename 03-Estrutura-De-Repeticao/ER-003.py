# Faça um programa que leia e valide as seguintes informações:
#       Nome: maior que 3 caracteres;
#       Idade: entre 0 e 150;
#       Salário: maior que zero;
#       Sexo: 'f' ou 'm';
#       Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Nome:   "))
idade = int(input("Idade:   "))
salario = float(input("Salário:   "))
sexo = str(input("Sexo:   ")).upper()
estcivil = str(input("Estado Civil:   ")).upper()
discr = [len(nome) < 4,
         idade < 1 or idade > 150,
         salario <= 0,
         sexo != "M" and sexo != "F",
         estcivil != "S" and estcivil != "C" and estcivil != "V" and estcivil != "D"].count(True)

while discr != 0:
    if discr[0]:
