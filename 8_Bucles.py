"""
Los bucles en Python son estructuras de control que 
permiten ejecutar un bloque de código repetidamente 
hasta que se cumple una condición o para cada elemento
 de una secuencia. Son fundamentales para automatizar tareas repetitivas.
"""

"""

Tipos de Bucles en Python
Python tiene dos tipos principales de bucles:

1. Bucle for
El bucle for se utiliza para iterar (recorrer) sobre una secuencia 
(como una lista, una tupla, un diccionario, un conjunto o una cadena) 
o sobre otros objetos iterables. Se usa cuando se conoce de antemano 
el número de veces que se quiere ejecutar el bloque de código 
(por ejemplo, el número de elementos en la lista).
"""

"""
for elemento in secuencia:
    # Bloque de código a ejecutar
    # con cada 'elemento' de la 'secuencia'
"""

# Iterar 5 veces (números del 0 al 4)
for i in range(5):
    print(f"Iteración número: {i}")

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Iterar desde 2 hasta 6 (números 2, 3, 4, 5, 6)
for num in range(2, 7):
    print(f"El número es: {num}")


"""
Bucle while 
El bucle while se utiliza para ejecutar un
 bloque de código mientras una condición sea verdadera
   (True). El bucle continuará ejecutándose 
   hasta que la condición se evalúe como falsa (False). 
   Es útil cuando no se sabe exactamente cuántas veces se debe
    repetir el bucle antes de comenzar.
"""

"""
while condicion_es_verdadera:
    # Bloque de código a ejecutar
    # ... debe haber una forma de que la condición cambie a False
"""

contador = 0
while contador < 3:
    print(f"El contador es: {contador}")
    contador += 1  # Incrementa el contador en 1 (paso crucial)

print("El bucle while ha terminado.")