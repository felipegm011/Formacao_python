import random

print("***********************************")
print("Bem vindo no jogo de adivinhação")
print("***********************************")
tentativas = 0
rodada = 0
numero_secreto = random.randrange(1,101)
print(numero_secreto)

print("Qual é o nível de dificuldade:")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Digite o nível: "))

if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
else:
    tentativas = 5


while (rodada < tentativas):
    
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
    # interpolação de string para inverte valores basta usar o indice que começa por 0 para o primero parametro
    print("** ", "Tentativa: {} de {} ".format(rodada, tentativas))

print("***********************************")
print("Fim de jogo")
print("***********************************")
