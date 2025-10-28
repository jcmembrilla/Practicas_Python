"""
Las varibales sirven para guardar datos en memoria
Python es un lenguaje de tipado dinamico y tipado 
fuerte
"""

#Para asignar una solo hace falta poner 
# el nombre de la variable + = + el valor
nombre = "Ale"
apellido = "Perez"
edad = 25

##Ejercicio 1 pintar por consola nombre, apellido y edad.
print("Nombre", nombre, "Apellido", apellido, "Edad", edad )

######### Hasta aca llegamos!!! #########

"""
Reglas: al escribir su nombre
- No pueden empezar con números.
- No usar espacios (usar guion bajo).
- Python distingue mayúsculas de minúsculas.
- No se púede usar guion medio (-)
"""

######### TEORIA #########

#Las variables se pueden reasignar
nombre = "Valentin"
apellido = "Ortiz"
edad = 20

"""
Tipado dinamico: Esto significa que el 
tipo de dato se determina en tiempo de 
ejecucion por lo tanto no hay que declararlo 
explicitamente
EJEMPLO:
"""
name = "Juan" #Declaramo una variable tipo string,
#lo estamos haciendo implicitamente, 
# al escribir un string
# sin la nececidad de remarcarlo.
print(type(name))

name = 32
print(type(name)) #Podemos ver como la misma variable 
#cambio dinamicamente de tipo. Los tipos de variables
# pueden cambiar en tiempo de ejecucion
#A diferencia de un tipado estatico, quiere decir que siempre va a tener ese tipo, ejm: string.

"""
Tipado Fuerte: Python no realiza conversiones de tipo automatico
Quiere decir que no va a forzar una conversion de tipo de dato
Ejemplo: 
"""
#print(10 + "12")
#Ejercicio copiar de la termial el mensaje de error y pegarlo aqui
#La terminal, muchas veces, es muy clara dandonos informacion 
#sobre del error que esta ocurriendo

"""
Convencion de nombres se utiliza sanake_case
simplemente separamos la siguiente palabra con guin bajo(_)
Ejemplo:

"""
este_es_el_nombre_de_la_variable = "correcto" #snake_case
nombre = "correcto"

NombreDeVariable = "No recomdable" #PascalCase
nombredevariable = "No recomendable" #sin ningun distintivo o separador

#True = False #No asignar nombres con las palabras reservadas del lenguaje
"""
Ejercicio: Con condicionales arrojar si es 
 correcto o incorrecto dependiendo del nombre de la variable
"""

is_user_loger: bool = True
print(is_user_loger)

#is_user_loger: bool = 42 #Cambia el tipo por mas que habilitemos 
print(is_user_loger)

