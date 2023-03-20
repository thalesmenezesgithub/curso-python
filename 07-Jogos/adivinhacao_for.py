print("********************************")
print("Bem-vindo ao Jodo de Adivinhação")
print("********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

for rodada in range(1, total_tentativas + 1):
    
    print("")
    
    #entrada de valores do usuário
    print("Tentativa {} de {} " .format(rodada,total_tentativas))
    chute_str = input("Digite um número entre 1 e 100 para advinhação:")
    print("Você digitou: ", chute_str)

    chute = int(chute_str)
    
     #verifica se o número e negativou ou  e maior que 100
    if(chute < 1 or chute > 100):
        print("Você deve digitar um valor entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto!")
            
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto!")
            
