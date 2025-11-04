#Función sin parámetros
"""
 Crea una función llamada presentacion() que imprima tu nombre y tu curso. Luego, llámala tres veces.
"""

def presentacio():
    print("Nombre, Sofia")
    print("Curso, Desarrollo Software")
   
presentacio()
presentacio()
presentacio()

#Función con un parámetro
"""
Define una función llamada despedir(nombre) que reciba un nombre y muestre un mensaje como:
Adiós, [nombre]. ¡Nos vemos pronto!"
Prueba la función con tres nombres diferentes.
"""

def despedir_a(nombre):
  print(f"Adios, {nombre}. Nos vemos pronto!")

despedir_a("Ana")
despedir_a("Maxi")
despedir_a("Juli")

#Función con dos parámetros
"""
Crea una función llamada multiplicar(a, b) que reciba dos números, calcule el producto y lo imprima.
"""

def multiplicar(a,b):
   multiplicar = a * b
   return multiplicar

print(multiplicar(8,8))

#Función con retorno de valor
"""
 Crea una función llamada elevar_al_cuadrado(numero) que reciba un número, calcule su cuadrado y retorne el resultado.
 Luego, guarda ese valor en una variable y muéstralo por pantalla.
 """
numero = (4)

def elevar_al_cuadrado(numero):
   return numero **2

resultado = elevar_al_cuadrado(numero)


#Función que use otra función
"""
Usando la función del ejercicio anterior (elevar_al_cuadrado), crea otra función llamada mostrar_cuadrado(numero) que use la función anterior para obtener el cuadrado y luego imprima el mensaje: "El cuadrado de [numero] es [resultado]".
"""

