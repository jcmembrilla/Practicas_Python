# 1. Crea una lista con varios números repetidos y usa count() para saber cuántas veces aparece el número 5.
lista_numeros = [7, 5, 9, 5, 1, 4, 5, 5, 8]
repet = lista_numeros.count(5)
print(repet)

# 2. En una tupla de nombres de colores, usa index() para saber en qué posición está el color "verde".
colores = ("azul", "verde", "amarillos", "blanco", "negro", "violeta")
color_index = colores.index("verde")
print(color_index)

# 3. Declara una lista con nombres de animales y muestra cuántos elementos tiene con len().
animales = ("gato", "delfin", "gorrion", "tigre", "cebra", "perro")
longitud_animales = len(animales)
print(longitud_animales)

# 4. Crea una lista con números enteros y muestra el número más grande y el más chico usando max() y min().
numeros = [15, 451, 19, 12, 501, 99]
min_numero = min(numeros)
max_numero = max(numeros)
print(f"Numero menor: {min_numero}. Numero mayor: {max_numero}.")

# 5. Dada una tupla con valores numéricos, calcula el total usando sum().
numeros_tupla = (142, 151, 519, 123, 51, 77)
suma_numeros_tupla = sum(numeros_tupla)
print(f"Suma de elementos de la tupla suma_numeros_tupla: {suma_numeros_tupla}")

# 6. Crea una lista de edades y muestra la lista ordenada de menor a mayor y luego de mayor a menor con sorted().
lista_edades = [21, 34, 32, 24, 30, 26, 31, 25, 30]
sort_menor_mayor = sorted(lista_edades)
sort_mayor_menor = sorted(lista_edades, reverse=True)
print(f"Lista ordenada de menor a mayor: f{sort_menor_mayor}")
print(f"Lista ordenada de mayor a menor: f{sort_mayor_menor}")

# 7. Desafío integrador: dada la lista valores = [10, 20, 10, 30, 40, 10, 50]:
#    - Muestra cuántas veces aparece el número 10.
#    - Indica en qué posición aparece por primera vez.
#    - Muestra la cantidad total de elementos.
#    - Calcula el máximo, el mínimo y la suma de todos.
#    - Muestra la lista ordenada de menor a mayor.
valores = [10, 20, 10, 30, 40, 10, 50]
print(f"""
      {valores}.
      El 10 aparece {valores.count(10)} en la lista.
      El 10 aparece por primera vez en la posicion {valores.index(10)}.
      La lista valores tiene {len(valores)} elementos.
      De la lista valores, el numero menor es {min(valores)}, el mayor {max(valores)}, y la suma de los elementos es {sum(valores)}.
      Lista ordenada de menor a mayor: {sorted(valores)}.
      Lista ordenada de mayor a menor: {sorted(valores, reverse=True)}.
""")