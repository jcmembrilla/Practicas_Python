### 
# Funciones 
# Bloques de codigo reutilizable y parametrizables para hacer tareas especificas


"""
Definicion
def nombre_de_la_funcion(parametro1, parametro2, ...)
#Cuerpo de la funcion
#return valor_de_la_funcion #opcional

"""

# Ejemplo de una funcion para impromir algo en consola
def saludar():
    print("Hola!")
#Aca solo la definimos, la creamos

#RECORDAR a las funciones simpre tenemos que llamarlas, invocarlas.
#Sino, no van a ejecutarce.

#Una ves que ya esta creada, podemos llamarla todas la veces que queramos.
saludar()
saludar()
saludar()


### Funcion con parametros ###
def saludar_a(nombre): #Declaramos el paramtro
    print(f"Hola {nombre}")

saludar_a("Pedro")#Le pasamos el argumento que queramos
saludar_a("Juan")
saludar_a("Maria")
#Podemos ver como comienza a tener sentido crear una funcion
#Solo pasandole un argumento se ejecuta el bloque de codigo 
# que preparamos, que ya pensamos y esta esperando que lo usemos.
#Con un solo parametro podemos pasarles diferentes argumentos.


# Funcion con mas parametros #

def sumar(a,b):
    suma = a + b
    return suma

print(sumar(4,4))#Llamamos la funcion directamente 

#En esta caso guardamos el resultado en una variable
resultado = sumar(2,2)
print(resultado)