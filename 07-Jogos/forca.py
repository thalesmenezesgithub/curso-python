def jogar():

    print("**************************")
    print("Bem-vindo ao Jodo de Forca")
    print("**************************")
    
    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou  = False
    
    print(letras_acertadas)

    while(not enforcou and not acertou):  
        chute = input("Qual letra?")
        chute = chute.strip() #remove os espaços
        
        indice = 0
        for letra in palavra_secreta:
            
            if chute.upper() == letra.upper():
                letras_acertadas[indice] = letra
                
            indice = indice + 1
        
        print(letras_acertadas)
            
            
if(__name__ == "__main__"):
    jogar()