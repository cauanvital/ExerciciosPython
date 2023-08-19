# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link
# de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam = float(input("Insira o tamanho do arquivo em MB:   "))
vel = float(input("Insira a velocidade da sua internet:   "))
tem = tam / vel / 60

print(f"Este arquivo levará aproximadamente {round(tem + 0.5)} minutos para ser instalado.")
