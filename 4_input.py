"""
Entrada de datos por input()
La funcion input() permite leer datos que ingresa
el usuario por teclado
ejemplo: nombre = input("Ingrese su nombre")

"""

"""
Ejercicio 9: Calcular el promedio de 3 notas que el usuario
ingrese por teclado
"""


calificacion_1 = int(input("Ingrese calificacion 1: "))
calificacion_2 = int(input("Ingrese calificacion 2: "))
calificacion_3 = int(input("Ingrese calificacion 3: "))

promedio = (calificacion_1 + calificacion_2+calificacion_3) / 3
print("El promedio es:", promedio) #A corregir. 
#Como en este caso si nos interesa los decimelas aplicamos float a promedio.

"""
Teoria:
Conversión de tipos de datos
Para convertir valores usamos:
- int() → convierte a número entero.
- float() → convierte a número decimal.
- str() → convierte a texto.
Ejemplo:
edad = int(input("Ingrese su edad: "))
print("Tu edad es:", edad)
Importante: input() siempre devuelve una cadena de texto (string).
"""

"""
Ejercicio 11: Pedir dos números y mostrar operaciones.
"""


"""
Ejercicio 12 Averiguar datos.
Preguntarle a el usuario como se llama, una ves que sepas el nombre
saludarlo y preguntarle el apellido. Finalmente saludar a el usuario por su nombre completo.
"""

print("hola como es tu nombre")
nombre = input()
print("Hola", nombre, "como es tu apellido?")
apellido = input()
print("Un gusto conocerlo", nombre, apellido)





"""
Ejercicio 13:
Pedir año de nacimiento y calcular edad.
"""

