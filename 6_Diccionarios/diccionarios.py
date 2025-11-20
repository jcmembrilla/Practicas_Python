"""
Los diccionarios son colecciones de mapeo que almacenan datos en forma de pares clave-valor.
Clave (Key): Actúa como un identificador único, similar a un índice o etiqueta, y debe ser inmutable
(generalmente una cadena de texto o un número).
Valor (Value): Es el dato asociado a esa clave, y puede ser cualquier tipo de objeto en Python 
(otro diccionario, una lista, un número, una cadena, etc.).
Sintaxis: Se definen utilizando llaves ({}) y los pares clave-valor se separan por dos puntos (:).

Los diccionarios son ideales para modelar objetos o registros de información donde cada pieza de
datos necesita una etiqueta descriptiva.

Sirven principalmente para:

Almacenar Registros: Modelar entidades del mundo real (una persona, un coche, un producto, etc.) 
donde cada atributo tiene un nombre específico.
Búsquedas Rápidas: Recuperar información de manera extremadamente rápida. 
Acceder a un valor por su clave es una operación muy eficiente.
Configuración: Almacenar ajustes o parámetros de configuración de forma legible y estructurada.
"""

# Un diccionario para almacenar la información de un usuario
perfil_usuario = {
    "nombre": "Elena",
    "edad": 30,
    "ciudad": "Argentina",
    "hobbies": ["leer", "viajar", "programar"]
}

# Acceder a un valor específico usando la clave
print(f"El nombre del usuario es: {perfil_usuario['nombre']}") 
# Salida: El nombre del usuario es: Elena

# # Acceder a un elemento dentro de la lista de hobbies
# print(f"Su primer hobby es: {perfil_usuario['hobbies'][0]}")
# # Salida: Su primer hobby es: leer

# # Modificar el valor de una clave existente (Mutabilidad)
# perfil_usuario["edad"] = 31 
# print(f"Nueva edad: {perfil_usuario['edad']}")
# # Salida: Nueva edad: 31

# # Añadir una nueva clave-valor
# perfil_usuario["es_premium"] = True
# print(perfil_usuario) 
# # Salida: {'nombre': 'Elena', 'edad': 31, 'ciudad': 'Argentina', 'hobbies': ['leer', 'viajar', 'programar'], 'es_premium': True}

print("--- 1. Iterar solo las CLAVES ---")
#Cuando se usa un bucle for directamente sobre un diccionario (perfil_usuario en este caso), 
# Python lo interpreta automáticamente como si estuvieras iterando sobre las claves del diccionario.
for clave in perfil_usuario:
    # También podrías usar: for clave in perfil_usuario.keys():
    valor = perfil_usuario[clave] # Usamos la clave para obtener el valor
    print(f"Clave: **{clave}**")


print("\n--- 2. Iterar solo los VALORES ---")
for valor in perfil_usuario.values():
    print(f"Valor: **{valor}**")

print("\n--- 3. Iterar CLAVES y VALORES (.items()) ---")
for clave, valor in perfil_usuario.items():
    print(f"La **{clave}** del usuario es: {valor}")

