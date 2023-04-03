import random

def jogar():

    print("**************************")
    print("Bem-vindo ao Jodo de Forca")
    print("**************************")

    frutas = ["pera", "uva", "goiaba", "manga","abacate","morango","banana","tomate","abacaxi","acerola","amora","cereja"]
    
    palavra_secreta = random.choice(frutas).upper()

    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou  = False
    erros = 0
    
    print("")
    print(letras_acertadas)

    while(not enforcou and not acertou):  
        chute = input("Qual letra?")
        chute = chute.strip().upper() #remove os espaços
        
        if(chute in palavra_secreta):

            indice = 0
            for letra in palavra_secreta:
            
                if chute == letra:
                    letras_acertadas[indice] = letra
                    
                indice = indice + 1
        
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
            print("Foi enforcado!")


if(__name__ == "__main__"):
    jogar()