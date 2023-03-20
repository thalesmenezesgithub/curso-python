import adivinhacao
import forca

print("****************")
print("Escolha seu Jogo")
print("****************")

print("(1) Forca ou (2) Adivinhação")
jogo = int(input("Qual o Jogo?"))

 #chama a função jogar do respectivo arquivo
if(jogo == 1):
    print("Jogando Forca!")
    forca.jogar()

elif(jogo == 2):
    print("Jogando Adivinhação!")
    adivinhacao.jogar()