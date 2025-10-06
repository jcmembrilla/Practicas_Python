"""
Las varibales sirven para guardar datos en memoria
Python es un lenguaje de tipado dinamico y tipado fuerte
"""

#Para asignar una solo hace falta poner el nombre de la variable + = + el valor
nombre = "Ale"
apellido = "Perez"
edad = 25

##Ejercicio 1 pintar por consola nombre, apellido y edad.
print("Nombre", nombre, "Apellido", apellido, "Edad", edad )

######### Hasta aca llegamos!!! #########

"""
Reglas:
- No pueden empezar con números.
- No usar espacios (usar guion bajo).
- Python distingue mayúsculas de minúsculas.

"""

######### TEORIA #########

#Las variables se pueden reasignar
nombre = "Valentin"
apellido = "Ortiz"
edad = 20

"""
Tipado dinamico: Esto significa que el tipo de dato se determina en tiempo de ejecucion
EL TIPO DE DATO SE DETERMINA EN TIEMPO DE EJECUCION
por lo tanto no hay que declararlo explicitamente
EJEMPLO:
"""
name = "Juan" #Declaramo una variable tipo string
print(type(name))

name = 32
print(type(name)) #Podemos ver como la misma variable cambio dinamicamente de tipo.
#Los tipos de variables pueden cambiar en tiempo de ejecucion
#A diferencia de un tipado estatico, quiere decir que siempre va a tener ese tipo, ejm: string.