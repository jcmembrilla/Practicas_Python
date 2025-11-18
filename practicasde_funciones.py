# Ejercicios sobre funciones
#1. Función sin parámetros
# Crea una función llamada presentacion() que imprima tu nombre y tu curso. Luego, llámala tres veces.

# def presentacion(nombre):
#     nombre = (input("hola: ingrese su nombre"))
#     print(f"Hola {nombre}")
# presentacion("santiago")
# presentacion("Juan")
# presentacion("mateo")


#2. Función con un parámetro
#Define una función llamada despedir(nombre) que reciba un nombre y muestre un mensaje como:
# "Adiós, [nombre]. ¡Nos vemos pronto!"
#Prueba la función con tres nombres diferentes.


# def despedir(nombre_chau):
#     print(f"adios, {nombre_chau}")
# despedir("roman")
# despedir("lionel")
# despedir("diego")

# 3. Función con dos parámetros Crea una función llamada multiplicar(a, b) que reciba dos números, calcule el producto y lo imprima.

# def multiplicar(a, b):
#     producto = a * b
#     print("el resultado de la multiplicacion es:",producto)
# multiplicar(10,7)

# 4. Función con retorno de valor
#  Crea una función llamada elevar_al_cuadrado(numero) que reciba un número, calcule su cuadrado y retorne el resultado.
#  Luego, guarda ese valor en una variable y muéstralo por pantalla.


# def elevar_al_cuadrado(numero):
#     cuadrado = numero ** 2
#     return cuadrado
# resultado = elevar_al_cuadrado(8)
# print(" su valor es:" , resultado)
    

# 5. Función que use otra función
#  Usando la función del ejercicio anterior (elevar_al_cuadrado), crea otra función llamada mostrar_cuadrado(numero) que use la función anterior para obtener el cuadrado y luego imprima el mensaje:
#  "El cuadrado de [numero] es [resultado]".


# def elevar_al_cuadrado(numero):
#     cuadrado = numero ** 2
#     return cuadrado

# def mostrar_cuadrado(numero):
#     resultado = elevar_al_cuadrado(numero)
#     print("El cuadrado de", numero, "es", resultado)

# mostrar_cuadrado(12)

# 6. Función con parámetros por teclado
#  Crea una función llamada saludo_personalizado() que no reciba parámetros, pero que pida el nombre del usuario con input() y luego muestre un saludo con ese nombre.

# def saludo_personalizado():
#     nombre = input("decime tu nombre")
#     print(f"como estas?{nombre}")
# saludo_personalizado()

# 7. Función que retorne más de un valor
#  Define una función llamada operaciones(a, b) que devuelva la suma y la resta de esos dos números.
#  Luego, muestra los resultados así:
# suma, resta = operaciones(10, 5)
# print("Suma:", suma)
# print("Resta:", resta)

# def operaciones(a, b):
#     suma = a + b
#     resta = a - b
#     return suma, resta
# suma, resta = operaciones(15, 8)
# print("suma", suma)
# print("resta", resta)


# 8. Función que combine lógica simple
#  Crea una función llamada es_par(numero) que retorne True si el número es par y False si es impar.
#  Luego, usa esa función en un programa que pida un número y diga por pantalla si es par o impar.


# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# numero = int(input("Ingresa un número: "))

# if es_par(numero):
#     print("El número es par.")
# else:
#     print("El número es impar.")
