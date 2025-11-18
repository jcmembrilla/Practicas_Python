# ## Ejercicio 1: Creación y Acceso a Diccionario 
# Objetivo: Practicar la creación de un Diccionario (dict) y la recuperación de valores por clave.

# Crea un diccionario llamado datos_libro con las siguientes claves y valores:

# "titulo": "El Gran Gatsby"

# "autor": "F. Scott Fitzgerald"

# "año": 1925

# "paginas": 208

# Accede al valor de la clave "autor" e imprímelo.
datos_libro = {
    "titulo": "El Gran Gatsby",
    "autor": "F. Scott Fitzgerald",
    "año": 1925,
    "paginas": 208
}
print(datos_libro["autor"])
# Añade un nuevo par clave-valor: "genero" con el valor "Novela".
datos_libro["genero"] = "Novela"
# Imprime el diccionario completo.
print(datos_libro)
# ## Ejercicio 2: Iteración con Diccionario (.items()) 
# Objetivo: Practicar la iteración simultánea de claves y valores usando el método .items().

# Usa el diccionario datos_libro del ejercicio anterior.

# Crea un bucle for que recorra el diccionario usando el método .items().

# Dentro del bucle, imprime la clave y el valor en el siguiente formato: [Clave]: [Valor].
for key, value in datos_libro.items():
    print(f"{key}: {value}.")


# ## Ejercicio 3
# Objetivo: Practicar la modificación de valores existentes y la eliminación de una clave en un diccionario, 
# seguido de una iteración.
# Crea un diccionario llamado inventario para un pequeño negocio, que almacene el stock de tres productos:

# "pan": 100

# "leche": 50

# "huevos": 30

# El cliente compra todo el stock de pan. Actualiza el valor de la clave "pan" a 0.

# El producto "huevos" será descontinuado. Elimina la clave "huevos" del diccionario.

# Crea un bucle for que recorra el diccionario usando el método .items().

# Dentro del bucle, imprime solo los productos cuyo stock sea mayor a 0.
inventario = {
    "pan": 100,
    "leche": 50,
    "huevos": 30
}
inventario["pan"] = 0
del inventario["huevos"]
for key, value in inventario.items():
    if value > 0:
        print(f"{key}: {value}.")
print(inventario)