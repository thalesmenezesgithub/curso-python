import random

def jogar():

    print("********************************")
    print("Bem-vindo ao Jodo de Adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000


    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível do jogo: "))

    # Nível de dificuldade
    if(nivel == 1):
        total_tentativas = 20
        
    elif(nivel == 2):
        total_tentativas = 10

    else:
        total_tentativas = 5
        
    rodada = 1    

    while(rodada <= total_tentativas):
        
        print("")
        
        #entrada de valores do usuário
        print("Tentativa {} de {} " .format(rodada,total_tentativas))
        chute_str = input("Digite um número entre 1 e 100 para advinhação:")

        chute = int(chute_str)
        
        #verifica se o número e negativou ou  e maior que 10
        if(chute < 1 or chute > 100):
            print("Você deve digitar um valor entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("|----------------------------------------|")
            print("| PARABÊNS VOCÊ ACERTOU E FEZ {} PONTOS! |".format(pontos))
            print("|----------------------------------------|")
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto!")
                
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto!")
                
            pontos_perdidos = abs(numero_secreto - chute)            
            pontos = pontos - pontos_perdidos
                
        rodada = rodada + 1

if(__name__ == "__main__"):
    jogar()