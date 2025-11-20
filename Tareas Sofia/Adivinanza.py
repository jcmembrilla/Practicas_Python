#crear un juego que adivine del 1 al 10
#se puede usar random
#usar pistas para que el usuario vaya adivinando
#nosotros tenemos que adivinar el numero por la terminal.

import random
numero_secreto = random.randint(1,10)

print("Adivina el numero que estoy pensando")

while True:
    tu_numero = int(input("Elegi un numero del 1 al 10 :"))

    if tu_numero > numero_secreto:
        print("Uno menos")
    elif tu_numero < numero_secreto:
        print("Uno mas")
    else:
        print("Adivinaste")
        break
