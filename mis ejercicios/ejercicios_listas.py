"""
Crea una lista llamada frutas con los elementos "manzana", "banana", "pera" y "naranja". 
Luego imprime el segundo elemento de la lista."""
""
#frutas = ["manzana", "banana", "pera", "naranja"] 

# print(frutas[1])
"""
Usando la lista anterior, imprime el último elemento utilizando un índice negativo.
"""
# print(frutas[-1])

"""
Crea una lista llamada numeros con los valores del 1 al 6.
Muestra solo los números del 2 al 4 utilizando slicing.
"""
num = [ 1, 2, 3, 4, 5, 6]
# print(num[1:4])

"""
Con la lista numeros, imprime los tres primeros elementos usando slicing.
"""
# print(num[:3])

"""
Muestra los tres últimos elementos de la lista numeros utilizando slicing.
"""
# print(num[3:])
"""
Crea una lista llamada pares con los números del 2 al 10.
Imprime solo los números que estén en posiciones pares (usa el parámetro paso en slicing).
"""
# pares = [ 2, 4, 6, 8, 10]
# print(pares[::2])
"""
Crea una lista reversa con los números del 1 al 5 e imprímela al revés utilizando slicing con paso negativo.
"""
# reversa = [1, 2, 3, 4, 5]
# print(reversa[::-1])
"""
Crea una lista colores = ["rojo", "verde", "azul"] y cambia el primer color por "amarillo".
"""
# colores = ["rojo", "verde", "azul"]
# colores[0] = "amarillo"
# print(colores)
"""
Crea una lista vacía llamada animales y agrégale tres animales usando el método append().
"""
# animales = []
# animales.append("pato")
# animales.append("mono")
# animales.append("gato")
# print(animales)
"""
Crea una lista letras = ["b", "c", "d"] e inserta la letra "a" al comienzo usando insert().
"""
# letras = ["b", "c", "d"]
# letras.insert(0, "a")
# print(letras)
"""
Crea una lista numeros = [1, 2, 3] y agrega al final los números 4, 5 y 6 usando el método extend().
"""
# numeros = [1, 2, 3]
# numeros.extend([4, 5, 6])
# print(numeros)
"""
Crea una lista borrar = ["uno", "dos", "tres", "cuatro"] 
y elimina el elemento "dos" usando remove().
"""
# borrar = ["uno", "dos", "tres", "cuatro"]
# borrar.remove("dos")
# print(borrar)

"""
Crea una lista palabras = ["hola", "chau", "adiós"] y elimina el último elemento con pop().
Muestra cuál fue el elemento eliminado.
"""
# palabras = ["hola", "chau", "adiós"]
# ultimo = palabras.pop()
# print("elemento eliminado", ultimo)
# print(palabras)
"""
Crea una lista elementos = ["a", "b", "c", "d"] y 
elimina el segundo elemento (índice 1) usando del.
"""
# elementos = ["a", "b", "c", "d"]
# del elementos[1]
# print(elementos)

"""
Crea una lista numeros = [10, 20, 30, 40, 50] 
y muestra en pantalla cuántos elementos tiene la lista usando la función len().
"""
numeros = [10, 20, 30, 40, 50]
print(f"Cantidad de elementos de la lista {len(numeros)}")
