"""
Bucle for:
El bucle for se utiliza para iterar (recorrer) sobre una secuencia 
(como una lista, una tupla, un diccionario, un conjunto o una cadena) 
o sobre otros objetos iterables. Se usa cuando se conoce de antemano 
el número de veces que se quiere ejecutar el bloque de código 
(por ejemplo, el número de elementos en la lista).
"""

"""
for elemento in secuencia:
    # Bloque de código a ejecutar
    # con cada 'elemento' de la 'secuencia'
"""

# Simple iteracion de lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Iterar desde 2 hasta 6 (números 2, 3, 4, 5, 6)
# Con estos parametros le decimos desde donde y hasta donde queremos que itere
for num in range(2, 7):
    print(f"El número es: {num}")

#Como podemos ver en este caso no le estamos 
# dando ninguna condicion o como se tiene que incrementar
# simplemete queremos que itere la lista y se lo ordenamos.

### Con for vamos a poder iterar sobre las cosas que puedan ser iterables ###
# Ejemplo una cadena de texto
cadena = "Cadena de texto"
for caracter in cadena:
    print(caracter)

# Iterar 5 veces (números del 0 al 4) usando range
for i in range(5):
    print(f"Iteración número: {i}")