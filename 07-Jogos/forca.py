import random

def mensagem_abertura():
    print("**************************")
    print("Bem-vindo ao Jodo de Forca")
    print("**************************")

def gera_palavra_secreta():
    
    frutas = ["pera", "uva", "goiaba", "manga","abacate","morango","banana","tomate","abacaxi","acerola","amora","cereja","jaca"]
    palavra_secreta = random.choice(frutas).upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):

    letras_acertadas = ["_" for letra in palavra_secreta]

    return letras_acertadas

def imprime_mensagem(acertou, palavra_secreta):
    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def verifica_acerto_palavra(letras_acertadas, palavra_secreta):

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

    imprime_mensagem(acertou, palavra_secreta)


def jogar():

    mensagem_abertura()

    palavra_secreta = gera_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    verifica_acerto_palavra(letras_acertadas, palavra_secreta)


if(__name__ == "__main__"):
    jogar()