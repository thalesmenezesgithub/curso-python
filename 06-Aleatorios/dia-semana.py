from datetime import datetime
import calendar

#data atual
data_atual = datetime.now()

#exibe a data atual
print("Data atual: ",data_atual)

#função verifica qual o dia da semana será retornado
def determina_semana():
    
    dia_semana = data_atual.weekday()
    
    if(dia_semana == 0):
        dia = "Segunda-Feira"
    
    elif(dia_semana == 1):
        dia = "Terça-Feira"

    elif(dia_semana == 2):
        dia = "Quarta-Feira"
    
    elif(dia_semana == 3):
        dia = "Quinta-Feira"
    
    elif(dia_semana == 4):
        dia = "Sexta-Feira"
    
    elif(dia_semana == 5):
        dia = "Sexta-Feira"
    
    else:
        dia = "Domingo"
    
    return dia

#exibe o dia da semana
print("Dia da semana: ",determina_semana())