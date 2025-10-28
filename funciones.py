


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