# Uma academia deseja fazer um senso entre os seus clientes para descobrir o mais alto, o mais baixo, o mais gordo e o
# mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia o seu código, sua
# altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais
# gordo e do mais magro, além da média das alturas e dos pesos dos clientes

i = 1

codverify = ""
sumPeso = 0
sumAltura = 0
qtdCliente = 0

pesoMenor = None
cPesMenor = 0

pesoMaior = None
cPesMaior = 0

alturaMenor = None
cAlturMenor = 0

alturaMaior = None
cAlturMaior = 0

while i == 1:
    cod = int(input("\nCódigo do cliente:   "))

    # Verifica se o código de cliente já foi inserido antes
    if codverify.find(f" {cod}") != -1:
        print("Este código já foi inserido. Tente outro")
        continue
    codverify = f"{codverify} {cod}"

    # Encerra o programa se for inserido o número 0
    if cod == 0:
        break

    # Define os valores de peso e altura
    peso = float(input("Peso do cliente:   "))
    altura = float(input("Altura do cliente:   "))

    if pesoMenor is None:
        pesoMenor = peso
        pesoMaior = peso
        alturaMenor = altura
        alturaMaior = altura
        cPesMenor = cPesMaior = cAlturMaior = cAlturMenor = cod

    # Define o menor peso
    if peso < pesoMenor and cod != 0:
        pesoMenor = peso
        cPesMenor = cod
    # Define o maior peso
    if peso > pesoMaior and cod != 0:
        pesoMaior = peso
        cPesMaior = cod

    # Define a menor altura
    if altura < alturaMenor and cod != 0:
        alturaMenor = altura
        cAlturMenor = cod
    # Define a maior altura
    if altura > alturaMaior and cod != 0:
        alturaMaior = altura
        cAlturMaior = cod

    # Define os valores para calcular as médias de peso e altura
    sumPeso += peso
    sumAltura += altura
    qtdCliente += 1

mediaPes = sumPeso / qtdCliente
mediaAlt = sumAltura / qtdCliente

print(f"\nCliente mais leve:\n"
      f"    Código: {cPesMenor}\n"
      f"    Peso: {pesoMenor}")
print(f"\nCliente mais pesado:\n"
      f"    Código: {cPesMaior}\n"
      f"    Peso: {pesoMaior}")
print(f"\nCliente mais baixo:\n"
      f"    Código: {cAlturMenor}\n"
      f"    Altura: {alturaMenor}")
print(f"\nCliente mais alto:\n"
      f"    Código: {cAlturMaior}\n"
      f"    Altura: {alturaMaior}")
print(f"\nA média do peso dos clientes é {mediaPes}, e a média da altura é {mediaAlt}")
