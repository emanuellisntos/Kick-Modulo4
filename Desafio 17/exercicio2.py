# 2. Faça um programa em que o usuário precisa cadastrar nome, idade, telefone e e-mail. Depois mostre os valores digitados na tela.

print("-- Formulário de Cadastro --")
print("Insira os seguintes dados")
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
telefone = input("Digite o seu telefone: ")
email = input("Digite o seu email: ")

print("\nDados cadastrados:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Telefone: {telefone}")
print(f"E-mail: {email}")
