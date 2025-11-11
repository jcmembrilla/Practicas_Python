#9  hacer una funcion que haga un juego que adivine un numero del 1 al 10

import random

def adivina_un_numero():
    numero_secreto = random.randint(1, 10)  # 👈 el número se genera una sola vez
    contador3 = 0

    
    while contador3 < 10:
        contador3 += 1
        
        numero = int(input(" elige un numero del 1 al 10 y adivina :  "))
    
        if numero == numero_secreto:
            print(f" el numero elegido es el correcto  {numero_secreto}")

            break

        else :

            print(f"sigue intentando  . Intento {contador3}/10. Seguí intentando...\n")

    else :
        
        print("se agotaron los intentos . El número era {numero_secreto}.") 
    

adivina_un_numero()            