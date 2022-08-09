from tkinter import Y


def jogar_forca():
    print("***********************************")
    print("Bem vindo no jogo da forca")
    print("***********************************")

    letras_acertadas = ["_","_","_","_","_","_"]

    palavra_secreta = "python"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        #strip remove espaçoes vazios na string
        entrada = input("Digite uma letra: ".strip())

        index = 0
        for letra in palavra_secreta:
            if(entrada.lower() == letra.lower()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
                letras_acertadas[index] = letra
            index = index + 1
        
        print(letras_acertadas)
        print("Jogondo")


    print("***********************************")
    print("Fim de jogo")
    print("***********************************")

if(__name__ == "__main__"):
    jogar_forca()