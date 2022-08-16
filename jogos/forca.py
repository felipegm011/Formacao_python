from tkinter import Y
import random

def jogar_forca():
    print("***********************************")
    print("Bem vindo no jogo da forca")
    print("***********************************")
    
    #abrindo arquivo e lendo primeiro param nome do arquivo segundo modificador de acesso
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    #fechando o arquivo
    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].lower()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        
        #strip remove espaçoes vazios na string
        entrada = input("Digite uma letra: ".strip())

        if(entrada.lower() in palavra_secreta.lower()):
            index = 0
            for letra in palavra_secreta:
                if(entrada.lower() == letra.lower()):
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1
        # verificando se a variavel erro é igual a 6 se sim enforcou recebe true
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("Jogondo")
    if(acertou):
        print("Você Ganhou")
    else:
        print("Você Perdeu")
    print("***********************************")
    print("Fim de jogo")
    print("***********************************")

if(__name__ == "__main__"):
    jogar_forca()