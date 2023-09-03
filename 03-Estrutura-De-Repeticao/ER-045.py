# Desenvolver um programa para verificar a nota do aluno numa prova com 10 questões, o programa deve perguntar ao
# aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
# nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#       Maior e Menor Acerto;
#       Total de Alunos que utilizaram o sistema;
#       A Média das Notas da Turma.
#           Gabarito da Prova:
#           01 — A
#           02 — B
#           03 — C
#           04 — D
#           05 — E
#           06 — E
#           07 — D
#           08 — C
#           09 — B
#           10 — A
#
#       Após concluir isto, você poderia incrementar o programa permitindo que o professor digite o gabarito da prova
#       antes dos alunos usarem o programa.

gab = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
alunoExperto = acertosAlunoExpert = alunoBurro = acertosAlunoBurro = None
i = qtdAlunos = sumAcertos = 0
codverify = ""

while True:
    insGabarito = str(input("Deseja inserir um gabarito próprio (\"S\" para SIM e \"N\" para NÃO)? ")).upper()

    if insGabarito == "N":
        break
    elif insGabarito == "S":

        # Estrutura para validar o gabarito se inserido pelo usuário
        while i < 10:
            gab[i] = str(input(f"Insira a resposta correta da pergunta {i + 1}: ")).upper()
            if gab[i] != 'A' and gab[i] != 'B' and gab[i] != 'C' and gab[i] != 'D' and gab[i] != 'E':
                print("Opção Inválida! Insira \"A\", \"B\", \"C\", \"D\" ou \"E\"")
                continue
            else:
                i += 1
        break
    else:
        print("Opção Inválida! Digite \"S\" para SIM ou \"N\" para NÃO")
        continue

while True:
    i = 0
    acertos = 0
    idAluno = int(input("\nInsira o ID de estudante (digite \"0\" para finalizar): "))

    if idAluno == 0:
        break

    # Verifica se o id do aluno já foi inserido
    if codverify.find(f" {idAluno}") != -1:
        print("Este aluno já respondeu ao teste")
        continue
    codverify = f"{codverify} {idAluno}"

    while i < 10:
        r = str(input(f"Insira a resposta da pergunta {i + 1}: ")).upper()
        if r != 'A' and r != 'B' and r != 'C' and r != 'D' and r != 'E':
            print("Resposta Inválida! Insira \"A\", \"B\", \"C\", \"D\" ou \"E\"")
            continue

        if i == 0 and r == gab[i]:
            acertos += 1
        elif i == 1 and r == gab[i]:
            acertos += 1
        elif i == 2 and r == gab[i]:
            acertos += 1
        elif i == 3 and r == gab[i]:
            acertos += 1
        elif i == 4 and r == gab[i]:
            acertos += 1
        elif i == 5 and r == gab[i]:
            acertos += 1
        elif i == 6 and r == gab[i]:
            acertos += 1
        elif i == 7 and r == gab[i]:
            acertos += 1
        elif i == 8 and r == gab[i]:
            acertos += 1
        elif i == 9 and r == gab[i]:
            acertos += 1

        i += 1

    sumAcertos += acertos
    qtdAlunos += 1

    if alunoExperto is None:
        alunoExperto = alunoBurro = idAluno
        acertosAlunoExpert = acertosAlunoBurro = acertos

    if acertos > acertosAlunoExpert:
        alunoExperto = idAluno
        acertosAlunoExpert = acertos
    if acertos < acertosAlunoBurro:
        alunoBurro = idAluno
        acertosAlunoBurro = acertos

media = sumAcertos / qtdAlunos

print(f"\nA média das notas dos alunos inseridos foi de {media:.1f}")
print(f"O aluno com mais acertos foi o número {alunoExperto}, tirando nota {acertosAlunoExpert:.1f}")
print(f"O aluno com menos acertos foi o número {alunoBurro}, tirando nota {acertosAlunoBurro:.1f}")
