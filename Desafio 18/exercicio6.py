# 6. Faça um programa em que o usuário digita um número inteiro e o programa exibe todos os números ímpares do 1 até o valor inserido.

numero = int(input("Digite um número inteiro: ")) 

contagem = range(1, numero + 1, 2)

for i in contagem:
    print(i)
