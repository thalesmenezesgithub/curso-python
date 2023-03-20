entrada = input("Digite um número inteiro: ")
numero = int(entrada)


if(numero % 15 ) == 0:
    print("FizzBuzz")
       
elif(numero % 3) == 0 :
    print("Fizz")
    
elif(numero % 5) == 0:
    print("Buzz")