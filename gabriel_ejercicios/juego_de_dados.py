#cada jugador tira dos veces el dado se suma y el que tiene mas grande el valor gana

import random

   
def jugada_de_dados():
    suma = 0
    for i in range(2):
        numero_dado = random.randint(1, 6)
        print(f"Tirada {i+1}: {numero_dado}")
        suma += numero_dado
    return suma  
    
participante1=input("ingrese su nombre :")
participante2=input("ingrese su nombre :")

print("Jugador 1 tira los dados:")
jugador1 = jugada_de_dados()
print(f"Suma total {participante1}: {jugador1}\n")

print("Jugador 2 tira los dados:")
jugador2 = jugada_de_dados()
print(f"Suma total {participante2}: {jugador2}\n")     
      
if jugador1 > jugador2:
    print(f"gana el {participante1} con :  {jugador1}\n")
elif jugador1 < jugador2 :
    print(f"gana el {participante2} con :  {jugador2}\n")
else: 
    print("estan empatados")
    
 

