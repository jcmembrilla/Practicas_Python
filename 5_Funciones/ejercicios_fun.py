# 1. Función sin parámetros
def presentacion():
    print("Mi nombre es Juan y curso 2° año de secundaria técnica.")

presentacion()
presentacion()
presentacion()

# 2. Función con un parámetro
def despedir(nombre):
    print(f"Adiós, {nombre}. ¡Nos vemos pronto!")

despedir("Pedro")
despedir("María")
despedir("Lucía")

# 3. Función con dos parámetros
def multiplicar(a, b):
    producto = a * b
    print(f"El resultado de multiplicar {a} x {b} es {producto}")

multiplicar(3, 4)
multiplicar(5, 6)

# 4. Función con retorno de valor
def elevar_al_cuadrado(numero):
    resultado = numero ** 2
    return resultado

cuadrado = elevar_al_cuadrado(5)
print(f"El cuadrado de 5 es {cuadrado}")

# 5. Función que use otra función
def elevar_al_cuadrado(numero):
    return numero ** 2

def mostrar_cuadrado(numero):
    resultado = elevar_al_cuadrado(numero)
    print(f"El cuadrado de {numero} es {resultado}")

mostrar_cuadrado(8)
# 6. Función con parámetros por teclado
def saludo_personalizado():
    nombre = input("Ingrese su nombre: ")
    print(f"¡Hola {nombre}! Bienvenido al curso de programación.")

saludo_personalizado()
# 7. Función que retorne más de un valor
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

suma, resta = operaciones(10, 5)
print("Suma:", suma)
print("Resta:", resta)
# 8. Función que combine lógica simple
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False



num = int(input("Ingrese un número: "))

if es_par(num):
    print("El número es par.")
else:
    print("El número es impar.")


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Ingrese un número: "))

if es_par(num):
    print("El número es par.")
else:
    print("El número es impar.")


# 5. Función que use otra función

def elevar_al_cuadrado(numero):
    return numero ** 2

def mostrar_cuadrado(numero):
    resultado = elevar_al_cuadrado(numero)
    print(f"El cuadrado de {numero} es {resultado}")

numero_de_usuario = int(input("Ingrese un numero: "))
mostrar_cuadrado(numero_de_usuario)



# ##Juego##

# import random

# # 1. Generar un número secreto entre 1 y 10 (ambos inclusive)
# numero_secreto = random.randint(1, 10)

# # Inicializar el contador de intentos y la bandera de juego
# intentos = 0
# adivinado = False

# print("¡Bienvenido al Juego de Adivinar el Número!")
# print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinarlo?")

# # 2. Bucle principal del juego
# while not adivinado:
#     try:
#         # Pedir al usuario que ingrese su suposición
#         suposicion = int(input("Ingresa tu suposición: "))
#         intentos += 1

#         # 3. Comprobar la suposición
#         if suposicion < numero_secreto:
#             print("Demasiado bajo. ¡Intenta de nuevo!")
#         elif suposicion > numero_secreto:
#             print("Demasiado alto. ¡Intenta de nuevo!")
#         else:
#             # Si es correcto, terminar el juego
#             print(f"\n¡Felicidades! ¡Adivinaste el número {numero_secreto} en {intentos} intentos!")
#             adivinado = True
            
#     except ValueError:
#         # Manejar el caso donde el usuario no ingresa un número
#         print("Entrada no válida. Por favor, ingresa un número entero.")