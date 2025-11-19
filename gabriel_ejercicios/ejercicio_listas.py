
# 1 crear una lista llamada frutas con los elementos "manzana , "banana" , "pera" , "naranja" 
#  1 luego imprime el segundo elemento de la lista
frutas = ["manzana" , "banana" , "pera" , "naranja"]
print(frutas[1])
#2 usando la lista anterior imprime el ultimo valor utilizando un indice negativo
print(frutas[-1])
#crea una lista llamada numeros con los valores de 1 al 6
#  3 muestra los valores del 2 al 4
numeros =[1,2,3,4,5,6]
print(numeros[2:5])
#  4 con la lista numeros muestra los tres primeros usando slicing
print(numeros[:4])
#  5  muestra los tres ultimos numeros usando slicing
print(numeros[3:])

#6. Crea una lista llamada pares con los números del 2 al 10.
pares = [2,3,4,5,6,7,8,9,10]
#Imprime solo los números que estén en posiciones pares (usa el parámetro paso en slicing).
print(pares[::2])
#7. Crea una lista reversa con los números del 1 al 5 e imprímela al revés utilizando slicing con paso negativo.
reversa = [1,2,3,4,5]
print(reversa[:-1])
#8. Crea una lista colores = ["rojo", "verde", "azul"] y cambia el primer color por "amarillo".
colores = ["rojo", "verde", "azul"]
#9. Crea una lista vacía llamada animales y agrégale tres animales usando el método append().
animales = []
animales.append("perro")
animales.append("gato")
animales.append("raton")
print(animales)
#10. Crea una lista letras = ["b", "c", "d"] e inserta la letra "a" al comienzo usando insert().
letras = ["b", "c", "d"]
print(letras)
letras.insert(0,"a")
print(letras)

#11. Crea una lista numeros = [1, 2, 3] y agrega al final los números 4, 5 y 6 usando el método extend().
numeros1 = [1, 2, 3]
print(numeros1)
numeros1.extend([4,5,6])
print(numeros1)
#12. Crea una lista borrar = ["uno", "dos", "tres", "cuatro"] y elimina el elemento "dos" usando remove().
borrar = ["uno", "dos", "tres", "cuatro"]
print(borrar)
borrar.remove("dos")
print(borrar)
#13. Crea una lista palabras = ["hola", "chau", "adiós"] y elimina el último elemento con pop().
#Muestra cuál fue el elemento eliminado.
palabras1 = ["hola", "chau", "adiós"]
print(palabras1)
palabras1.pop(-1)
print(palabras1)

#14. Crea una lista elementos = ["a", "b", "c", "d"] y elimina el segundo elemento (índice 1) usando del.
elementos = ["a", "b", "c", "d"]
print(elementos)
del elementos[1]
print(elementos)
#15. Crea una lista numeros = [10, 20, 30, 40, 50] y muestra en pantalla cuántos elementos tiene la lista usando la función len().
numeros2 = [10, 20, 30, 40, 50]
print(numeros2)
print(len(numeros2))