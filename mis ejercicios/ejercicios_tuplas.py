"""
1. Inmutabilidad:
Creá una tupla llamada numeros con cinco valores.
Intentá cambiar el segundo elemento por otro valor y observá el error que aparece.
"""
# numeros = (25, 33, 92, 10, 3)
# numeros[1]= 4

"""
2. Acceso y recorrido:
Creá una tupla llamada animales con tres nombres de animales.
a) Mostrá el primer y el último elemento.
b) Recorrela con un bucle for para imprimir cada animal.
"""
animales = ("pato", "mono", "jirafa")
print(animales[0])
print(animales[2])
i = 1
for animal in animales:
    print(f"{i}. Animal: {animal}")
    i += 1
"""
3. Conversión lista <-> tupla:
Convertí la tupla animales en una lista, agregá un nuevo elemento, y luego volvé a convertirla en tupla.
Mostrá la tupla resultante.
"""
lista_animales = list(animales)
lista_animales = lista_animales + ["gato"]
animales = tuple(lista_animales)
i = 1
for animal in animales:
    print(f"{i}. Animal: {animal}")
    i += 1

"""
4. Uso como clave en un diccionario:
Creá un diccionario llamado coordenadas donde las claves sean tuplas que representen posiciones (x, y) y los valores sean nombres de ciudades.
Luego imprimí el valor asociado a una de esas coordenadas.
"""
coordenadas = {
    (1,2) : "Ayacucho",
    (3,4) : "Mar del Plata",
    (5,6) : "Tandil"
}

print(coordenadas[(1,2)])