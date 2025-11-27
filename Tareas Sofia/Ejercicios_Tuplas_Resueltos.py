#1. Inmutabilidad:
"""
Creá una tupla llamada numeros con cinco valores.
Intentá cambiar el segundo elemento por otro valor y observá el error que aparece.
"""

numeros = (10,20,30,40,50)
#numeros.remove(1)
#numeros.insert(1,25)
print(numeros) 
#no entiendo bien, no funciona


#2. Acceso y recorrido:
"""
Creá una tupla llamada animales con tres nombres de animales.
a) Mostrá el primer y el último elemento.
b) Recorrela con un bucle for para imprimir cada animal.
"""

animales_tuple = ("gato","perro","conejo")

print(animales_tuple[0])
print(animales_tuple[-1])

for animales in animales_tuple:
    print(animales)

#3. Conversión lista <-> tupla:
"""
Convertí la tupla animales en una lista, agregá un nuevo elemento, y luego volvé a convertirla 
en tupla.
Mostrá la tupla resultante.
"""
animales = ("gato", "perro", "conejo") #esto es una tupla!!!!

animales = [animales]# esto es una lista...
animales.append("serpiente") #le agrego otro elemento con "append" que sirve para agregar elementos al final de la lista
animales = (animales) #esto vuelve a ser una tupla...

print(animales)
#los corchetes son para las listas, los parentesis para las tuplas



#4. Uso como clave en un diccionario:
"""
Creá un diccionario llamado coordenadas donde las claves sean tuplas que representen posiciones (x, y) y los valores sean nombres de ciudades.
Luego imprimí el valor asociado a una de esas coordenadas.
"""

coordenadas = {(10,20) : "buenos aires", (20,30) : "cordoba"}
print(coordenadas[(10,20)])
#las claves son key 
#los valores son value

#usan llaves para definir un diccionarios y los corchetes para los valores!....
# y dos puntos para separar, ------> clave:valor
