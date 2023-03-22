def jogar():

    print("**************************")
    print("Bem-vindo ao Jodo de Forca")
    print("**************************")
    
    palavra_secreta = "banana"
    enforcou = False
    acertou  = False
    
    while(not enforcou and not acertou):  
        chute = input("Qual letra?")
        chute = chute.strip() #remove os espaços
        
        indice = 0
        for letra in palavra_secreta:
            
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {}".format(letra, indice))
                print(chute)
                
            indice = indice + 1
            
            
            
if(__name__ == "__main__"):
    jogar()