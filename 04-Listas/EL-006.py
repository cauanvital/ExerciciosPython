# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o
# número de alunos com média maior ou igual a 7,0.

alunos = {}
notas = []
media = []

for i in range(10):
    for j in range(4):
        notas.append(float(input(f"{j + 1}ª nota do {i + 1}º aluno: ")))

    alunos[i] = notas
    media.append(sum(alunos[i]) / len(alunos[i]))
    notas = []
    print()

filtrados = [x for x in media if x >= 7]
print(f"Número de alunos com média maior ou igual a 7.0: {len(filtrados)}")
