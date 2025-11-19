"""
1. Función sin parámetros
 Crea una función llamada presentacion() que imprima tu nombre y tu curso. Luego, llámala tres veces.
"""
# def presentacion ():
#     print("Sandra Divasson")
#     print("Diplomatura de Desarrollo de Software")

# presentacion()
# presentacion()
# presentacion()

"""
2. Función con un parámetro
 Define una función llamada despedir(nombre) que reciba un nombre y muestre un mensaje como:
 "Adiós, [nombre]. ¡Nos vemos pronto!"despedir(nombre)
 Prueba la función con tres nombres diferentes.

"""
# def despedir(nombre):
#     print(f"Adiós {nombre}. ¡Nos vemos pronto!") 

# despedir("Juan")
# despedir("Mauricio")
# despedir("Gaston")
"""
3. Función con dos parámetros
 Crea una función llamada multiplicar(a, b) que reciba dos números, calcule el producto y lo imprima.
"""
# def multiplicar(a,b):
#     producto= a*b
#     return producto

# print(f"Resultado de la multiplicación: {multiplicar(2,5)}")
"""
4. Función con retorno de valor
 Crea una función llamada elevar_al_cuadrado(numero) que reciba un número, calcule su cuadrado y retorne el resultado.
 Luego, guarda ese valor en una variable y muéstralo por pantalla.
"""
# def elevar_al_cuadrado(numero):
#     cuadrado = numero ** 2
#     return cuadrado

# resultado= elevar_al_cuadrado(3)
# print(f"El cuadrado de 3 es {resultado}")

"""
5. Función que use otra función
 Usando la función del ejercicio anterior (elevar_al_cuadrado), crea otra función llamada 
 mostrar_cuadrado(numero) que use la función anterior para obtener el cuadrado y luego imprima el mensaje:
 "El cuadrado de [numero] es [resultado]".
"""
# def elevar_al_cuadrado(numero):
#     cuadrado = numero ** 2
#     return cuadrado

# def mostrar_cuadrado(numero):
#     print(f"El cuadrado de {numero} es {elevar_al_cuadrado(numero)}")
    
# print(mostrar_cuadrado(3))
"""
6. Función con parámetros por teclado
 Crea una función llamada saludo_personalizado() que no reciba parámetros, pero que pida el nombre
  del usuario con input() y luego muestre un saludo con ese nombre.
"""
# def saludo_personalizado():
#     nombre = input("Ingrese su nombre.")
#     print(f"Bienvenido {nombre}")

# saludo_personalizado()
"""
7. Función que retorne más de un valor
 Define una función llamada operaciones(a, b) que devuelva la suma y la resta de esos dos números.
 Luego, muestra los resultados así:
suma, resta = operaciones(10, 5)
print("Suma:", suma)
print("Resta:", resta)
"""
# def operaciones(a, b):
#     suma = a+b
#     resta= a-b
#     return suma, resta
# print(f"suma, resta: {operaciones(2,5)}")
# def operaciones(a, b):
#     suma = a+b
#     resta= a-b
#     return suma, resta
# resultados = operaciones(2,5)
# print(f"suma= {resultados[0]}")
# print(f"resta= {resultados[1]}")
"""
8. Función que combine lógica simple
 Crea una función llamada es_par(numero) que retorne True si el número es par y False si es impar.
 Luego, usa esa función en un programa que pida un número y diga por pantalla si es par o impar.
"""
# def es_par(numero):
#     resto = numero%2
#     if resto == 0:
#         print(f"El número {numero} es par.")
#     else:
#         print(f"El número {numero} es impar.")

# es_par(1)
# es_par(2)
"""
9. Creaer un juego que adivine un numero del 1 al 10
"""
import random

def generar_numero():
    """Genera y devuelve un número secreto entre 1 y 10."""
    return random.randint(1, 10)

def pedir_intento():
    """Pide al usuario un número y lo devuelve como entero."""
    return int(input("Ingresa un número del 1 al 10: "))

def jugar():
    numero_secreto = generar_numero()
    print("¡Adivina el número del 1 al 10!")

    while True:
        intento = pedir_intento()

        if intento == numero_secreto:
            print("¡Correcto, adivinaste el número!")
            break
        elif intento < numero_secreto:
            print("El número es más alto, intenta otra vez.")
        else:
            print("El número es más bajo, intenta de nuevo.")

# Llamamos a la función principal
jugar()


