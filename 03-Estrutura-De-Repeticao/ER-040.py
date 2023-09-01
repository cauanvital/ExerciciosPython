# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos
# os seguintes dados:
#       Código da cidade;
#       Número de veículos de passeio (em 1999);
#       Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#       Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence;
#       Qual a média de veículos nas cinco cidades juntas;
#       Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

i = mediaVeiculo = contMenos2000 = somaMenos2000 = 0
codverify = ""
maisAcidente = menosAcidente = codMaisAcidente = codMenosAcidente = None

while i < 5:
    cod = int(input("\nCódigo da cidade: "))

    if codverify.find(f" {cod}") != -1:
        print("Este código já foi inserido. Tente outro")
        continue
    codverify = f"{codverify} {cod}"

    nVeiculo = int(input("Número de veículos de passeio (em 1999): "))
    nAcidente = int(input("Número de acidentes de trânsito com vítimas (em 1999): "))

    if nVeiculo < 2000:
        contMenos2000 += 1
        somaMenos2000 += nVeiculo

    if maisAcidente is None:
        codMaisAcidente = codMenosAcidente = cod
        maisAcidente = menosAcidente = nAcidente

    if nAcidente > maisAcidente:
        maisAcidente = nAcidente
        codMaisAcidente = cod
    if nAcidente < menosAcidente:
        menosAcidente = nAcidente
        codMenosAcidente = cod

    mediaVeiculo += nVeiculo / 5
    i += 1

print(f"\nA cidade com maior índice de acidentes é a cidade {codMaisAcidente}, com {maisAcidente} acidentes.")
print(f"A cidade com menor índice de acidentes é a cidade {codMenosAcidente}, com {menosAcidente} acidentes.")
print(f"\nA média total de veículos entre as 5 cidades é {mediaVeiculo}")

if contMenos2000 > 0:
    print(f"A média de acidentes entrea as cidades com menos de 2000 veículos é de {somaMenos2000 / contMenos2000}")
