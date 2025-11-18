### El bucle while permite ejecutar un bloque 
# de codigo repetidamete mientrasse cumpla una condicion ###

"""
Bucle while 
El bucle while se utiliza para ejecutar un
 bloque de código mientras una condición sea verdadera
   (True). El bucle continuará ejecutándose 
   hasta que la condición se evalúe como falsa (False). 
   Es útil cuando no se sabe exactamente cuántas veces se debe
    repetir el bucle antes de comenzar.
"""

"""
while condicion_es_verdadera:
    # Bloque de código a ejecutar
    # ... debe haber una forma de que la condición cambie a False
"""

# contador = 0
# #De esta forma podemos ver claramente la condicion de salida del bucle
# while contador < 3:
#     #Mientras la condicon se cumpla el bloque de codigo se va a ejecutar constantemente
#     print(f"El contador es: {contador}")
#     contador += 1  # Incrementa el contador en 1 (paso crucial)


### Evitar bucles infinitos ###

#while True:
#    print("print infinito")

# Palabra reservada break, para cortar el bucle
#Cuando no sabemos exactanmente la condicion de salida 
#Podemos utilizar break para que procese, hasta encontrar esa condicion.
# contador2 = 0
# while True:
#     print(contador2)
#     contador2 += 1
#     if contador2 == 5:
#         break # Orden para salir del bucle

##palabre reservada continue: hace saltar esa iteraccion en concreto 
# y continua con el bucle

contador3 = 0
while contador3 < 10:
    contador3 += 1

    if contador3 % 2 == 0: #Si es par continua
        continue
    #Si la condicion se cumple pasa directamnte a la siguiente ocndicion
    print(contador3)
