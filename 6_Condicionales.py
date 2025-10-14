"""
Las sentecias condicionales permiten ejecutar 
codigo solo si se cumplen ciertas condiciones 
(if, elif, else)
"""

#Sentencia condicional basica

edad = 15

if edad >= 18: #Los dos puntos reprecentan un "entonces"
    print("Eres mayor de edad")#Delimitamos lo que se va a ejecutar con una tabulacion
    print("Tu edad es", edad)
    print("Bloque que se ejecuta")#Todo o que esta a este nivel se ejecuta si cumle con la condicion


#Sentecias if - else
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Sentecias if - elif - else
#Simulacion de calificaciones
nota = 10
if nota >= 9:
    print("Exelente!")
elif nota >=7:
    print("Muy bien!")
elif nota >= 4:
    print("Aprobado")
else:
    print("Desaprobado")

"""
Importante! una ves que se cumple una de la condiciones 
arrojara ese resultado, obviando las otras posibilidades
En el ejemlo de arriba podemos ver que si la nota seria 10
cumple con todas las condiciones, pero solo dara como respuesta 
la primera condicion que se cumpla, es este caso "Exelente!".
Por eso es importante en este caso, el orden de las condiciones.
"""

#En este ejemplo podemos ver la importancia del orden
nota = 10
if nota >= 4:
    print("Aprobado!") #Entra en esta condicon
elif nota >=7:
    print("Muy bien!")
elif nota >= 9:
    print("Exelente!") #Obvia esta por mas que la nota es 10
else:
    print("Desaprobado")


#Condiciones multiples
edad = 18
nacionaldiad = "argentino"

#and: Verifica que todas las condiciones se cumplan
if edad >= 16 and nacionaldiad == "argentino":
    print("puedes ejercer tu derecho al voto")

#or: En este caso solo se debe cumplir alguna 
# de las condiciones. Ya con que se de una, el resultado sera True
tv_propia = False
tv_amigo = True
if tv_propia or tv_amigo:
    print("Puedes mirar el partido")

#not: Invierte la condicion, Si una expresión es True, 
# not la convierte en False, y si es False, la convierte en True
es_verdad = True
no_es_verdad = not es_verdad
print(no_es_verdad)  # Output: False

es_falso = False
no_es_falso = not es_falso
print(no_es_falso)   # Output: True

esta_lloviendo = False
if not esta_lloviendo:
    print("Podemos salir afuera")

esta_abierto = False
if not esta_abierto:#Nos arroja un resultado True la condicion se cumple
    print("La tienda está cerrada.")#Es verdad que la tienda no esta abierta
