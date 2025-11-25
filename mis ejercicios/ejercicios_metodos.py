"""
1. Crea una lista con varios números repetidos y usa count() para saber cuántas veces aparece el número 5.
"""
numeros = [5,8,6,3,4,5,8,6,4,5]
print(numeros.count(5))
"""
2. En una tupla de nombres de colores, usa index() para saber en qué posición está el color "verde".
"""
colores = ("azúl", "rojo", "amarillo", "negro", "verde", "rosa", "blanco")
print(colores.index("verde"))
"""
3. Declara una lista con nombres de animales y muestra cuántos elementos tiene con len().
"""
animales = ["mono", "perro", "gato", "caballo", "vaca"]
print(len(animales))
"""
4. Crea una lista con números enteros y muestra el número más grande y el más chico usando max() y min().
"""
print(max(numeros))
print(min(numeros))
"""
5. Dada una tupla con valores numéricos, calcula el total usando sum().
"""
tupla_numeros = tuple(numeros)
print(sum(tupla_numeros))
"""
6. Crea una lista de edades y muestra la lista ordenada de menor a mayor y luego de mayor a menor con sorted().
"""
edades = [3,8,9,15,7,5,4,12,18]
print(sorted(edades))
print(sorted(edades, reverse=True))
"""
7. Desafío integrador: dada la lista valores = [10, 20, 10, 30, 40, 10, 50]:
   - Muestra cuántas veces aparece el número 10.
   - Indica en qué posición aparece por primera vez.
   - Muestra la cantidad total de elementos.
   - Calcula el máximo, el mínimo y la suma de todos.
   - Muestra la lista ordenada de menor a mayor.
"""
valores = [10, 20, 10, 30, 40, 10, 50]
print(valores.count(10))
print(valores.index(10))
print(len(valores))
print(max(valores))
print(min(valores))
print(sum(valores))
print(sorted(valores))