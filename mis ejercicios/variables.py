"""
Las variables sirven para guardar datos en menoria
Ppythin es un lenguaje de tipo dinamico y tipado fuerte.
"""
#Para asignar una sola hace falta poner
#el nombre de la variable + = + el valor

nombre = "Ale"
apellido = "Perez"
edad = 25

# Ejercicio 1 pintar por consola el nombre, apellido y edad
print("Nombre:", nombre, "Apellido:", apellido, "Edad:", edad)

"""
Reglas: al escribir su nombre 
-No pueden empezar con números.
-No usar espacios(usar guion bajo). 
-Pythin distingue mayusculas de minusculas.
- No se puede usar guion medio (-)
"""

#Las variables se pueden reasignar 
nombre = "valentin"
apellido = "Ortiz"
edad = 20

"""
Tipado dinamico: Esto significa que el 
tipo de dato se determina en tiempo de ejecucion 
por lo tando no hay qye declararlo explicitamente.
EJEMPLO:
"""
name = "Juan" #Declaramos una variable tipo string, 
#lo estamos haciendo implicitamente, 
#al escribir un string
# sinla necesidad de remarcarlo
print(type(name))

name = 32
print(type(name)) #podemos ver como la misma variable cambio 
#dinamicamente de tipo. Los tipos de variables pueden cambiar
#en tiempo de ejecucion. A diferencia de un tipado estatico, 
#quiere decir que siempre va a tener ese tipo, ejemplo: string. 

"""
Tipado Fuerte: Python no realiza conversaciones de tipo automatico
Quiere decir que no va a forzar una conversion de tipo de dato
Ejemplo:
"""
