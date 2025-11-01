"""
1. Función sin parámetros
 Crea una función llamada presentacion() 
 que imprima tu nombre y tu curso. Luego, llámala tres veces.
"""

def presentacion():
    print("Jeremias Ponce, desarrollo de software")

presentacion()
presentacion()
presentacion()

"""
2. Función con un parámetro
 Define una función llamada despedir(nombre) que reciba un nombre 
 y muestre un mensaje como:
 "Adiós, [nombre]. ¡Nos vemos pronto!"
 Prueba la función con tres nombres diferentes.
"""

def despedida(nombre):
    print(f"adios {nombre}")

despedida("ricardo")
despedida("manuel")
despedida("esteban")

"""
3. Función con dos parámetros
 Crea una función llamada multiplicar(a, b) 
 que reciba dos números, calcule el producto y lo imprima.
"""

def multiplicar(a,b):
    multiplicar = a * b
    return multiplicar

print(multiplicar(2,4))

"""
4. Función con retorno de valor
 Crea una función llamada elevar_al_cuadrado(numero) que reciba 
 un número, calcule su cuadrado y retorne el resultado.
 Luego, guarda ese valor en una variable y muéstralo por pantalla.
"""

def elevar_al_cuadrado(numero):
    elevar = numero **2
    return elevar
resultado2 = elevar_al_cuadrado(4)

print(f"el resultado es: {resultado2}")

"""
5. Función que use otra función
Usando la función del ejercicio anterior (elevar_al_cuadrado), 
crea otra función llamada mostrar_cuadrado(numero) que use la función
anterior para obtener el cuadrado y luego imprima el mensaje:
"El cuadrado de [numero] es [resultado]".
"""

def mostrar_cuadrado(numero):
    mostrar_cuadrado = resultado2

    print(f"el cuadrado de 4 es {resultado2}")