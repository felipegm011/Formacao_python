
import forca as forca
import adivinhacao as adivinhacao

print("***********************************")
print("Escolha seu jogo")
print("***********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("forca")
    forca.jogar_forca()
elif(jogo == 2):
    print("adivinhação")
    adivinhacao.jogar_adivinhacao()