# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

le = str(input("Digite uma letra:   ")).upper()

if not le.isalpha():
    print("Você não digitou apenas uma letra")
    exit()
elif len(le) > 1:
    print("Você digitou mais de um caractere")
    exit()

if le == "A" or le == "E" or le == "I" or le == "O" or le == "U":
    print("Você digitou uma vogal")
else:
    print("Você digitou uma consoante")

