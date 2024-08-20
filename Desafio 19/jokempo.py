import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    
    escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    while escolha_jogador not in opcoes:
        escolha_jogador = input("Escolha inválida. Tente novamente: ").lower()
    
    escolha_robo = random.choice(opcoes)
    print(f"Você escolheu: {escolha_jogador}")
    print(f"O robô escolheu: {escolha_robo}")
    
    if escolha_jogador == escolha_robo:
        print("Empate!")
    elif (escolha_jogador == "pedra" and escolha_robo == "tesoura") or \
         (escolha_jogador == "papel" and escolha_robo == "pedra") or \
         (escolha_jogador == "tesoura" and escolha_robo == "papel"):
        print("Você venceu! :)")
    else:
        print("Você perdeu! :(")

jogar()
