import random

print("***********************************")
print("Bem vindo no jogo de adivinhação")
print("***********************************")
tentativas = 3
rodada = 0

while (rodada < tentativas):
    numero_secreto = random.randrange(50)
    entrada = int (input("Digite seu número entre 1 e 100: "))

    if (entrada < 1 or entrada > 100):
        print("Voce digitou valor inválido")
        # não sai do laço ele só sai da iteração
        continue

    print("** ", "Seu chute foi: ", entrada)
    print("** ", "Número secreto: ", numero_secreto)

    if (entrada == numero_secreto):
        print("Acertou")
        # sai do laço
        break
    else:
        if(entrada > numero_secreto):
            print("Errou, seu chute foi maior que o número secreto")
        elif(entrada < numero_secreto):
            print("Errou, seu chute foi menor que o número secreto")
    rodada = rodada +1
    # interpolação de string 
    print("** ", "Tentativa: {} de {} ".format(rodada, tentativas))

print("***********************************")
print("Fim de jogo")
print("***********************************")
