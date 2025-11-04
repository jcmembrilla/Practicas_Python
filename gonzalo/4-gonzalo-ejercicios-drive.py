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
animales = []
animales.append("Gato")
animales.append("Perro")
animales.append("Loro")

# 10. Crea una lista letras = ["b", "c", "d"] e inserta la letra "a" al comienzo usando insert().
letras = ["b", "c", "d"]
letras.insert(0, "a")

# 11. Crea una lista numeros = [1, 2, 3] y agrega al final los números 4, 5 y 6 usando el método extend().
numeros = [1, 2, 3]
numeros.extend(4, 5, 6)

# 12. Crea una lista borrar = ["uno", "dos", "tres", "cuatro"] y elimina el elemento "dos" usando remove().
borrar = ["uno", "dos", "tres", "cuatro"]
borrar.remove("dos")

# 13. Crea una lista palabras = ["hola", "chau", "adiós"] y elimina el último elemento con pop().
# Muestra cuál fue el elemento eliminado.
palabras = ["hola", "chau", "adiós"]
ultimo = palabras.pop()
print(ultimo)

# 14. Crea una lista elementos = ["a", "b", "c", "d"] y elimina el segundo elemento (índice 1) usando del.
elementos = ["a", "b", "c", "d"]
del elementos[1]

# 15. Crea una lista numeros = [10, 20, 30, 40, 50] y muestra en pantalla cuántos elementos tiene la lista usando la función len().
numeros = [10, 20, 30, 40, 50]
print(len(numeros))

# Ejercicios While:
# 1.
#  Crea un programa que muestre los números del 0 al 4 utilizando un bucle while.
#  Pista: usa una variable llamada contador que comience en 0 y aumente en 1 en cada iteración.
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# 2.
#  Escribe un programa que pida al usuario una contraseña y siga pidiéndola mientras no sea igual a "python123".
#  Cuando la contraseña sea correcta, muestra el mensaje: "Acceso concedido".


# 3.
#  Crea un programa que utilice un bucle while para sumar los números del 1 al 5.
#  Debe mostrar al final: "La suma total es: X", donde X es el resultado de la suma.
# 4.
#  Escribe un programa que comience con un contador en 1 y muestre los números hasta 10,
#  pero detenga el bucle con break si el número es igual a 6.
#  Muestra un mensaje que diga "Bucle interrumpido en el número 6".
 
# Ejercicios for:
# 1.
#  Crea una lista llamada animales que contenga tres nombres de animales.
#  Luego, usa un bucle for para recorrer la lista e imprimir cada uno en pantalla.

# 2.
#  Utiliza range() para mostrar los números del 1 al 10, ambos inclusive,
#  usando un bucle for y el formato de impresión:
#  El número es: X.

# 3.
#  Crea una cadena de texto con tu nombre y usa un bucle for para recorrerla,
#  mostrando cada letra por separado en una nueva línea.

# 4.
#  Usando range(), realiza un bucle for que muestre las siguientes líneas:
# Iteración número: 0 
# Iteración número: 1 
# Iteración número: 2 
# Iteración número: 3 
# Iteración número: 4
# Pista: el bucle debe repetirse cinco veces.