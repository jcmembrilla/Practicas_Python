"""Ejercicios sobre funciones = BELEN ANTUNEZ
1. Función sin parámetros
 Crea una función llamada presentacion() que imprima tu nombre y tu curso. Luego, llámala tres veces.
"""

def presentacion():
    print("Mi nombre es Belen y cursando programacion")
presentacion()


"""
2. Función con un parámetro
 Define una función llamada despedir(nombre) que reciba un nombre y muestre un mensaje como:
 "Adiós, [nombre]. ¡Nos vemos pronto!"
 Prueba la función con tres nombres diferentes."""


def despedir(nombre):
    print(f"Adios, {nombre}. Nos vemos Pronto!")

despedir("Maria")
despedir("Pablo")
despedir("Jose")


"""
3. Función con dos parámetros
 Crea una función llamada multiplicar(a, b) que 
 reciba dos números, calcule el producto y lo imprima."""

def multiplicar(a,b):
    print(f"El resultado de multiplicar {a} x {b} es {a*b}")
multiplicar(2,3)

"""
4. Función con retorno de valor
 Crea una función llamada elevar_al_cuadrado(numero) que reciba un número, calcule su cuadrado y retorne el resultado.
 Luego, guarda ese valor en una variable y muéstralo por pantalla."""


def elevar_al_cuadrado(numero):
    resultado = numero ** 2
    return resultado

cuadrado = elevar_al_cuadrado(6)
print(f"El cuadrado de 6 es {cuadrado}")


#5. Función que use otra función
# Usando la función del ejercicio anterior (elevar_al_cuadrado), 
# crea otra función llamada mostrar_cuadrado(numero) que use la función anterior 
# para obtener el cuadrado y luego imprima el mensaje:
# "El cuadrado de [numero] es [resultado]".

def mostrar_cuadrado(numero):
    cuadrado = elevar_al_cuadrado(numero)
    print(f"El cuadrado de {numero} es: {cuadrado}")
mostrar_cuadrado(5)


#6. Función con parámetros por teclado
# Crea una función llamada saludo_personalizado() que no reciba parámetros, pero que pida el nombre del usuario con input() y luego muestre un saludo con ese nombre.
def saludo_personalizado():
    nombre = input("¿Cual es tu nombre?")
    print(f"Hola {nombre}")
saludo_personalizado()

#7. Función que retorne más de un valor
# Define una función llamada operaciones(a, b) que devuelva la suma y la resta de esos dos números.
# Luego, muestra los resultados así:
#suma, resta = operaciones(10, 5)
#print("Suma:", suma)
#print("Resta:", resta)

def operaciones(a,b):
    suma = a + b
    resta = a - b
    return suma, resta

suma, resta = operaciones(12,8)
print("Suma:", suma)
print("Resta:", resta)


#8. Función que combine lógica simple
# Crea una función llamada es_par(numero) que retorne True si el número es par y False si es impar.
# Luego, usa esa función en un programa que pida un número y diga por pantalla si es par o impar.

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
numero = int(input("Ingrese un numero:"))
if es_par(numero):
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

#
# 9. Crear un juego que adivine un numero del 1 al 10


def juego_adivinanza():
    numero_secreto = 7  # Número fijo para el juego (puedes cambiarlo)
    
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número del 1 al 10. ¡Adivínalo!")
    
    while True:  # Bucle infinito hasta que acierte
        adivinanza = int(input("Ingresa tu adivinanza (1-10): "))
        
        if adivinanza == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            break  # Sale del bucle
        else:
            print("Incorrecto. Intenta de nuevo.")

# Llamar a la función para iniciar el juego
juego_adivinanza()
