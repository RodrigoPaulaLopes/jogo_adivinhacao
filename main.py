import random
import os
print("###################################")
print("Bem vindo ao jogo de adivinhação")
print("###################################")
resposta = 's'
while resposta == 's':
    numero_secreto = random.randrange(1, 10, 1)


    chute = int(input("Digite o numero de 1 a 10: "))

    if chute == numero_secreto:
        print("Você acertou!")
    else:
        print("Lamento! Você errou.")
    print('numero secreto: {}'.format(numero_secreto))

    resposta = input("Deseja jogar novamente? (s/n)")
    os.system('cls')
print("Obrigado por jogar!")