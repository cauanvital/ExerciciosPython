# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vet1 = []
vet2 = []
vet3 = []
vet4 = []

for i in range(10):
    vet1.append(int(input("Insira um valor para o primeiro vetor: ")))

print()

for i in range(10):
    vet2.append(int(input("Insira um valor para o segundo vetor: ")))

print()

for i in range(10):
    vet3.append(int(input("Insira um valor para o terceiro vetor: ")))

for i in range(10):
    vet4.append(vet1[i])
    vet4.append(vet2[i])
    vet4.append(vet3[i])

print(f"\nPrimeiro vetor: {vet1}")
print(f"Segundo vetor: {vet2}")
print(f"Terceiro vetor: {vet3}")
print(f"Terceiro vetor: {vet4}")
