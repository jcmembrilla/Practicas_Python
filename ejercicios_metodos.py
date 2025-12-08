#Metodos: BELEN ANTUNEZ

#1. Crea una lista con varios números repetidos y usa count() para saber cuántas veces aparece el número 5.
numeros = [5, 5, 5, 5, 5, 5, 5]
print(numeros.count(5))

#2. En una tupla de nombres de colores, usa index() para saber en qué posición está el color "verde".
colores = ("rosa", "verde", "azul", "rojo", "violeta")
print(colores.index("verde"))

#3. Declara una lista con nombres de animales y muestra cuántos elementos tiene con len().
animales = ["lobo", "loro", "Elefante", "gato", "perro"]
print(len(animales))

#4. Crea una lista con números enteros y muestra el número más grande y el más chico usando max() y min().
num_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(num_enteros))
print(min(num_enteros))

#5. Dada una tupla con valores numéricos, calcula el total usando sum().
numeros = [21,34,55,66,77,88,99]
print(sum(numeros))

#6. Crea una lista de edades y muestra la lista ordenada de menor a mayor y luego de mayor a menor con sorted().
edades = [10, 20, 30, 40, 50]
print(sorted(edades))
print(sorted(edades, reverse=True))

#7. Desafío integrador: dada la lista valores = [10, 20, 10, 30, 40, 10, 50]:
  # - Muestra cuántas veces aparece el número 10.
  # - Indica en qué posición aparece por primera vez.
  # - Muestra la cantidad total de elementos.
  # - Calcula el máximo, el mínimo y la suma de todos.
  # - Muestra la lista ordenada de menor a mayor.

valores = [10, 20, 10, 30, 40, 10, 50]
print(valores.count(10))
print(valores.index(10))
print(len(valores))
print(max(valores))
print(min(valores))
print(sum(valores))
print(sorted(valores))