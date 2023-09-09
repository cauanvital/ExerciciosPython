# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade
# de organizações:
#       "Qual o melhor Sistema Operacional para uso em servidores?"
#
#       As possíveis respostas são:
#
#       1- Windows Server
#       2- Unix
#       3- Linux
#       4- Netware
#       5- Mac OS
#       6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
# mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser
# aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser
# armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de
# cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
#       Sistema Operacional     Votos   %
#       -------------------     -----   ---
#       Windows Server           1500   17%
#       Unix                     3500   40%
#       Linux                    3000   34%
#       Netware                   500    5%
#       Mac OS                    150    2%
#       Outro                     150    2%
#       -------------------     -----
#       Total                    8800
#
#       O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

print("Qual o melhor Sistema Operacional para uso em servidores?\n\n"
      "As possíveis respostas são:\n\n"
      "1 - Windows Server\n"
      "2 - Unix\n"
      "3 - Linux\n"
      "4 - Netware\n"
      "5 - Mac OS\n"
      "6 - Outro\n")

contagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

while True:
    voto = int(input("Voto: "))

    if voto == 0: break
    if voto < 0 or voto > 6:
        print("Inválido!")
        continue

    for i in contagem:
        if voto == i:
            contagem[i] += 1

porcentagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in porcentagem:
    porcentagem[i] = None if sum(contagem.values()) == 0 else round(contagem[i] / sum(contagem.values()) * 100, 1)

print("\nSistema Operacional   Votos   %\n"
      "-------------------   -----   ----\n"
      f"Windows Server        {contagem[1]}", " " * (6 - len(str(contagem[1]))), f"{porcentagem[1]}%\n"
      f"Unix                  {contagem[2]}", " " * (6 - len(str(contagem[2]))), f"{porcentagem[2]}%\n"
      f"Linux                 {contagem[3]}", " " * (6 - len(str(contagem[3]))), f"{porcentagem[3]}%\n"
      f"Netware               {contagem[4]}", " " * (6 - len(str(contagem[4]))), f"{porcentagem[4]}%\n"
      f"Mac OS                {contagem[5]}", " " * (6 - len(str(contagem[5]))), f"{porcentagem[5]}%\n"
      f"Outro                 {contagem[6]}", " " * (6 - len(str(contagem[6]))), f"{porcentagem[6]}%")
