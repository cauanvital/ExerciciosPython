# Numa eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
# utilizados são:
#       1 , 2, 3, 4  - Votos para os respectivos candidatos
#       (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#       5 - Voto Nulo
#       6 - Voto em Branco
#       Faça um programa que calcule e mostre:
#           O total de votos para cada candidato;
#           O total de votos nulos;
#           O total de votos em branco;
#           A percentagem de votos nulos sobre o total de votos;
#           A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor
#           zero.

qtdVotos = qtdVotoHuck = qtdVotoXarop = qtdVotoWilso = qtdVotoJean = qtdVotoNulo = qtdVotoBranco = 0

print("-=-= SUPER ELEIÇÃO BEM LEGAL QUE DEMAIS AIAIAIAIAI =-=-\n\n"
      "1 - Luciano Huck\n"
      "2 - Xaropinho\n"
      "3 - Sr. Senhor Wilson\n"
      "4 - Jean Carteiro Cósmico\n"
      "5 - Voto Nulo\n"
      "6 - Voto em Branco\n")

while True:
    voto = int(input(f"Insira o {qtdVotos + 1}º voto (digite \"0\" para finalizar a votação): "))
    if voto != 0 and voto != 1 and voto != 2 and voto != 3 and voto != 4 and voto != 5 and voto != 6:
        print("\nValor Inválido! Tente novamente")
    if voto == 0: break
    else: qtdVotos += 1

    if voto == 1:
        qtdVotoHuck += 1
    elif voto == 2:
        qtdVotoXarop += 1
    elif voto == 3:
        qtdVotoWilso += 1
    elif voto == 4:
        qtdVotoJean += 1
    elif voto == 5:
        qtdVotoNulo += 1
    elif voto == 6:
        qtdVotoBranco += 1

perNulo = qtdVotoNulo / qtdVotos * 100
perBranco = qtdVotoBranco / qtdVotos * 100

print("\nVOTAÇÃO ENCERRADA! O total de votos foi:\n"
      f"Luciano Huck: {qtdVotoHuck}\n"
      f"Xaropinho: {qtdVotoXarop}\n"
      f"Sr. Senhor Wilson: {qtdVotoWilso}\n"
      f"Jean Carteiro Cósmico: {qtdVotoJean}\n"
      f"Nulo: {qtdVotoNulo}\n"
      f"Em Branco: {qtdVotoBranco}\n"
      f"{perNulo}% dos votos foi nulo e {perBranco}% foi em branco")
