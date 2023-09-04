# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
# deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vet1 = []
vet2 = []
vet3 = []

for i in range(10):
    vet1.append(int(input("Insira um valor para o primeiro vetor: ")))

print()

for i in range(10):
    vet2.append(int(input("Insira um valor para o segundo vetor: ")))
for i in range(10):
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print(f"\nPrimeiro vetor: {vet1}")
print(f"Segundo vetor: {vet2}")
print(f"Terceiro vetor: {vet3}")
