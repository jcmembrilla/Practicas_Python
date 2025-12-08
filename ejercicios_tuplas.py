#Tuplas = BELEN ANTUNEZ
"""
1. Inmutabilidad:
Creá una tupla llamada numeros con cinco valores.
Intentá cambiar el segundo elemento por otro valor y observá el error que aparece."""

numeros = (1, 2, 3, 4, 5)
print(numeros) 

numeros[1] = 99  #Cambio de valor / ERROR


"""
2. Acceso y recorrido:
Creá una tupla llamada animales con tres nombres de animales.
a) Mostrá el primer y el último elemento.
b) Recorrela con un bucle for para imprimir cada animal."""

animales = ("lobo", "pez", "rata")
print(animales[0], animales[-1]) #Primer y ultimo elemento

for animal in animales:
    print(animal)

"""
3. Conversión lista <-> tupla:
Convertí la tupla animales en una lista, agregá un nuevo elemento, y luego volvé a convertirla en tupla.
Mostrá la tupla resultante."""

animales = ("lobo", "pez", "rata")
animales = list(animales)
animales.append("gato")
animales = tuple(animales)
print(animales)

"""
4. Uso como clave en un diccionario:
Creá un diccionario llamado coordenadas donde las claves sean tuplas que representen posiciones (x, y) y los valores sean nombres de ciudades.
Luego imprimí el valor asociado a una de esas coordenadas."""

coordenadas ={
    (10,20):"Buenos Aires",
    (30,40):"Tandil",
    (50,60):"Mardel"
}

print(coordenadas[(30,40)])