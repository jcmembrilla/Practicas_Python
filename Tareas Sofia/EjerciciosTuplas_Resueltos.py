#1. Inmutabilidad:
"""
Creá una tupla llamada numeros con cinco valores.
Intentá cambiar el segundo elemento por otro valor y observá el error que aparece.
"""

tuple = (10,20,30,40,50)

print(tuple) 


#2. Acceso y recorrido:
"""
Creá una tupla llamada animales con tres nombres de animales.
a) Mostrá el primer y el último elemento.
b) Recorrela con un bucle for para imprimir cada animal.
"""

animales = ("gato","perro","conejo")
tuple = animales
print(tuple[0])
print(tuple[2])

for animales in tuple:
    print(animales)




#3. Conversión lista <-> tupla:
"""
Convertí la tupla animales en una lista, agregá un nuevo elemento, y luego volvé a convertirla en tupla.
Mostrá la tupla resultante.
"""

#4. Uso como clave en un diccionario:
"""
Creá un diccionario llamado coordenadas donde las claves sean tuplas que representen posiciones (x, y) y los valores sean nombres de ciudades.
Luego imprimí el valor asociado a una de esas coordenadas.
"""