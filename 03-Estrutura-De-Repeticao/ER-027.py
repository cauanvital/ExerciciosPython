# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

i = 1
soma = 0
qtdturm = int(input("Insira a quantidade de turmas:   "))

while qtdturm < 2:
    print("Valor Inválido! Insira uma quantidade maior que 1")
    qtdturm = int(input("Insira a quantidade de turmas:   "))

while i < qtdturm + 1:
    qtdalun = int(input(f"Insira a quantidade de alunos da {i}ª turma:   "))

    if qtdalun < 2 or qtdalun > 40:
        print("A turmas devem ter no mínimo 2 e no máximo 40 alunos")
        continue

    soma += qtdalun
    i += 1

media = soma / qtdturm

print(f"A média aritmética de alunos por turma é {media}")
