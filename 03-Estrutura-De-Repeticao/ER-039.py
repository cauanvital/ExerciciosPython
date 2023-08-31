# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
# alto e o número do aluno mais baixo, junto com suas alturas.

codverify = ""
i = 1
alunoMai = codAlMai = alunoMen = codAlMen = None

while i < 11:
    codAluno = int(input(f"\nInsira o número do {i}º aluno: "))

    if codverify.find(f" {codAluno}") != -1:
        print("Este código já foi inserido. Tente outro")
        continue
    codverify = f"{codverify} {codAluno}"

    altAluno = int(input(f"Insira o altura do {i}º aluno: "))

    if alunoMai is None:
        alunoMai = alunoMen = altAluno
        codAlMai = codAlMen = codAluno

    if altAluno > alunoMai:
        alunoMai = altAluno
        codAlMai = codAluno
    if altAluno < alunoMen:
        alunoMen = altAluno
        codAlMen = codAluno

    i += 1

print(f"\nAluno mais alto: número {codAlMai}, altura {alunoMai}")
print(f"Aluno mais baixo: número {codAlMen}, altura {alunoMen}")
