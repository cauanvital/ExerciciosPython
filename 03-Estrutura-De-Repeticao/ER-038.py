# Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
#       Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#       Em 1996 recebeu aumento de 1,5% sobre o seu salário inicial;
#       A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#       Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa
#       permitindo que o usuário digite o salário inicial do funcionário.

salario = float(input("Insira o valor inicial do salário: "))
aumento = 1.5
ano = 1995
anoatual = int(input("Insira o ano até onde foi dado aumento: "))

while ano < anoatual:
    salario += salario / 100 * aumento
    aumento *= 2
    ano += 1

print(f"O salario em {anoatual} é de R$ {salario:.2f}")
