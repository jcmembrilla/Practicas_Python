# Ejercicios sobre Listas en Python

# 1. Crea una lista llamada frutas con los elementos "manzana", "banana", "pera" y "naranja". Luego imprime el segundo elemento de la lista.
frutas = ["manzana", "banana", "pera", "naranja"]
print(frutas[1])

# 2. Usando la lista anterior, imprime el último elemento utilizando un índice negativo.
print(frutas[-1])

# 3. Crea una lista llamada numeros con los valores del 1 al 6.
# Muestra solo los números del 2 al 4 utilizando slicing.
numeros = [1, 2, 3, 4, 5, 6]
print(numeros[1:4])

# 4. Con la lista numeros, imprime los tres primeros elementos usando slicing.
print(numeros[:3])

# 5. Muestra los tres últimos elementos de la lista numeros utilizando slicing.
print(numeros[3:])

# 6. Crea una lista llamada pares con los números del 2 al 10.
# Imprime solo los números que estén en posiciones pares (usa el parámetro paso en slicing).
pares = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(pares[::2])

# 7. Crea una lista reversa con los números del 1 al 5 e imprímela al revés utilizando slicing con paso negativo.
reversa = [5, 4, 3, 2, 1]
print(reversa[::-1])
# 8. Crea una lista colores = ["rojo", "verde", "azul"] y cambia el primer color por "amarillo".
colores = ["rojo", "verde", "azul"]
colores[0] = "amarillo"
print(colores)

# 9. Crea una lista vacía llamada animales y agrégale tres animales usando el método append().

# 10. Crea una lista letras = ["b", "c", "d"] e inserta la letra "a" al comienzo usando insert().

# 11. Crea una lista numeros = [1, 2, 3] y agrega al final los números 4, 5 y 6 usando el método extend().

# 12. Crea una lista borrar = ["uno", "dos", "tres", "cuatro"] y elimina el elemento "dos" usando remove().

# 13. Crea una lista palabras = ["hola", "chau", "adiós"] y elimina el último elemento con pop().
# Muestra cuál fue el elemento eliminado.

# 14. Crea una lista elementos = ["a", "b", "c", "d"] y elimina el segundo elemento (índice 1) usando del.

# 15. Crea una lista numeros = [10, 20, 30, 40, 50] y muestra en pantalla cuántos elementos tiene la lista usando la función len().