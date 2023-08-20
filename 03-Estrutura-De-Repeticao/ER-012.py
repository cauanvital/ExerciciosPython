# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
# informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#       Tabuada de 5:
#       5 X 1 = 5
#       5 X 2 = 10
#       ...
#       5 X 10 = 50

n = int(input("Insira um número inteiro de 1 a 10:   "))
exit("Número inválido! Digite um número inteiro entre 1 e 10.") if n < 1 or n > 10 else None

print(f"Tabuada do {n}:")
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")
