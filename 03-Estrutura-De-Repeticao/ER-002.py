# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.

nome = str(input("Nome de usuário:   "))
senha = str(input("Senha:   "))

while nome.upper() == senha.upper():
    print("ERRO! Senha não pode ser igual ao nome de usuário, tente novamente")
    senha = str(input("Senha:   "))

print("Senha válida")
