# 1. Inmutabilidad:
# Creá una tupla llamada numeros con cinco valores.
# Intentá cambiar el segundo elemento por otro valor y observá el error que aparece.
numeros = (10, 40, 28, 51, 5)
#numeros[1] = 15
"""
TypeError: 'tuple' object does not support item assignment
"""

# 2. Acceso y recorrido:
# Creá una tupla llamada animales con tres nombres de animales.
# a) Mostrá el primer y el último elemento.
# b) Recorrela con un bucle for para imprimir cada animal.

animales = ("gato", "perro", "chita")
print(animales[0])
print(animales[-1])

for animal in animales:
    print(animal)

# 3. Conversión lista <-> tupla:
# Convertí la tupla animales en una lista, agregá un nuevo elemento, y luego volvé a convertirla en tupla.
# Mostrá la tupla resultante.
animales_lista  = list(animales)
animales_lista.append("gorrión")
nueva_tupla = tuple(animales_lista)
print(nueva_tupla)

# 4. Uso como clave en un diccionario:
# Creá un diccionario llamado coordenadas donde las claves sean tuplas que representen posiciones (x, y) y los valores sean nombres de ciudades.
# Luego imprimí el valor asociado a una de esas coordenadas.
coordenadas = {
    (15, 10): "Argentina",
    (10, 5): "Bolivia",
    (9, 10): "Perú"
}
print(coordenadas[(15, 10)])