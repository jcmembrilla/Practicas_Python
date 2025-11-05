# #Ejercicio prueba en la clase.
# name = input("Ingrese su nombre: ")

# def saludar(nombre):
#     print(f"Hola {nombre}!!!")

# saludar(name)
# Ejercicios sobre funciones
# 1. Función sin parámetros
#  Crea una función llamada presentacion() que imprima tu nombre y tu curso. Luego, llámala tres veces.

def presentacion():
    print("Gonzalo Cabrera")
    print("Diplomatura de desarrollo de software.")
presentacion()
presentacion()
presentacion()

# 2. Función con un parámetro
#  Define una función llamada despedir(nombre) que reciba un nombre y muestre un mensaje como:
#  "Adiós, [nombre]. ¡Nos vemos pronto!"
#  Prueba la función con tres nombres diferentes.

def despedir(nombre):
    print(f"Adiós, {nombre}. ¡Nos vemos pronto!")

despedir("María")
despedir("José")
despedir("Flor")
 
# 3. Función con dos parámetros
#  Crea una función llamada multiplicar(a, b) que reciba dos números, calcule el producto y lo imprima.
def multiplicar(a, b):
    print(f"El producto de {a} y {b} es {a*b}")

multiplicar(9, 6)
# 4. Función con retorno de valor
#  Crea una función llamada elevar_al_cuadrado(numero) que reciba un número, calcule su cuadrado y retorne el resultado.
#  Luego, guarda ese valor en una variable y muéstralo por pantalla.
def elevar_al_cuadrado(numero):
    return numero ** 2
numero = int(input("Ingresar un numero para clacular el cuadrado: "))
resultado = elevar_al_cuadrado(numero)
print(f"El resultado es {resultado}")

# 5. Función que use otra función
#  Usando la función del ejercicio anterior (elevar_al_cuadrado), crea otra función llamada mostrar_cuadrado(numero) que use la función anterior para obtener el cuadrado y luego imprima el mensaje:
#  "El cuadrado de [numero] es [resultado]".

def mostrar_cuadrado(numero, resultado):
    print(f"El cuadrado de {numero} es {resultado}.")

mostrar_cuadrado(numero, resultado)
# 6. Función con parámetros por teclado
#  Crea una función llamada saludo_personalizado() que no reciba parámetros, pero que pida el nombre del usuario con input() y luego muestre un saludo con ese nombre.

def saludar():
    name = input("Ingrese su nombre: ")
    print(f"Hola {name}!!!")

saludar()

# 7. Función que retorne más de un valor
#  Define una función llamada operaciones(a, b) que devuelva la suma y la resta de esos dos números.
#  Luego, muestra los resultados así:
# suma, resta = operaciones(10, 5)
# print("Suma:", suma)
# print("Resta:", resta)
def operaciones(a, b):
    return a + b, a - b
funcionsuma, funcionresta = operaciones(10, 5)
print("Suma:", funcionsuma)
print("Resta:", funcionresta)

# 8. Función que combine lógica simple
#  Crea una función llamada es_par(numero) que retorne True si el número es par y False si es impar.
#  Luego, usa esa función en un programa que pida un número y diga por pantalla si es par o impar.
numero_par = int(input("Ingrese un numero para saber si es par: "))
def es_par(numero):
    return numero % 2 == 0
print(es_par(numero_par))