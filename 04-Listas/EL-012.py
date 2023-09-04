# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

idade = []
altura = []
qtdAlunos = 0

for i in range(30):
    idade.append(int(input(f"Idade do {i + 1}º aluno: ")))
    altura.append(int(input(f"Altura do {i + 1}º aluno: ")))

media = sum(idade) / len(idade)

for i in range(30):
    if idade[i] > 13 and altura[i] < media:
        qtdAlunos += 1

print(f"Existem {qtdAlunos} alunos maiores de 13 anos abaixo da média de altura geral")
