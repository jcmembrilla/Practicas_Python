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

def elevar_al_cuadrado(numero):
   elevar = numero ** 2
   return elevar 
resultado2 = elevar_al_cuadrado(4)
   
print(f"el resultado es: {resultado2}")


#Función que use otra función
"""
Usando la función del ejercicio anterior (elevar_al_cuadrado), 
crea otra función llamada mostrar_cuadrado(numero) que use la 
función anterior para obtener el cuadrado y luego imprima el mensaje: "El cuadrado de [numero] es [resultado]".
"""

def mostrar_cuadrado(numero):
   resultado = elevar_al_cuadrado(numero)
   print(f"el cuadrado  de {numero} es {resultado}")

mostrar_cuadrado(6)


"""
Función con parámetros por teclado
Crea una función llamada saludo_personalizado() que no reciba parámetros, pero que pida el nombre del usuario con input() y luego muestre un saludo con ese nombre.
"""

def saludo_personalizado():
  nombre = input("Como es tu nombre? :")
  print(f"Hola {nombre}, mucho gusto")

saludo_personalizado()


"""
Función que retorne más de un valor
Define una función llamada operaciones(a, b) que devuelva la suma y la resta de esos dos números.
Luego, muestra los resultados así:
suma, resta = operaciones(10, 5)
print("Suma:", suma)
print("Resta:", resta)
"""

def operaciones(a, b):
   suma = a + b 
   resta = a - b
   return suma, resta

suma, resta = operaciones(10, 5)

print("Suma:", suma)
print("Resta:", resta)

"""
 Función que combine lógica simple
 Crea una función llamada es_par(numero) que retorne True si el número es par y False si es impar.
 Luego, usa esa función en un programa que pida un número y diga por pantalla si es par o impar.
"""

def es_par(numero):
    return numero % 2 == 0

numero = int(input("Numero: "))
print("Es par" if es_par(numero) else "Es impar")

