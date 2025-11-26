
# 1. Inmutabilidad:
#Creá una tupla llamada numeros con cinco valores.
#Intentá cambiar el segundo elemento por otro valor y observá el error que aparece.

#numeros = (10, 20, 30, 40, 50)
#print(numeros)
#numeros[1] = 99

#2. Acceso y recorrido:
#Creá una tupla llamada animales con tres nombres de animales.
#a) Mostrá el primer y el último elemento.
#b) Recorrela con un bucle for para imprimir cada animal.

#animales = ("perro", "gato", "loro")
#print(animales[0])  
#print(animales[-1]) 
#for animal in animales:
    #print(animal)

#3.Conversión lista <-> tupla:
#Convertí la tupla animales en una lista, agregá un nuevo elemento, y luego volvé a convertirla en tupla.
#Mostrá la tupla resultante.

#animales = ("perro", "gato", "loro")

#lista_animales = list(animales)

#lista_animales.append("tortuga")

#animales = tuple(lista_animales)

#print(animales)

#4. Uso como clave en un diccionario:
#Creá un diccionario llamado coordenadas donde las claves sean tuplas que representen posiciones (x, y) y los valores sean nombres de ciudades.
#Luego imprimí el valor asociado a una de esas coordenadas.

#coordenadas = {
    #(34, 56): "Buenos Aires",
    #(12, 90): "Córdoba",
    #(77, 23): "Rosario"
#}

#print(coordenadas[(12, 90)])

