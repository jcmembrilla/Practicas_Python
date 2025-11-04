#1. Función sin parámetros
 #Crea una función llamada presentacion() que imprima tu nombre y tu curso. Luego, llámala tres veces.
def presentacion() :
    print("gabriel")
    print("programacion")

presentacion()
presentacion()
presentacion() 

#2. Función con un parámetro
 #Define una función llamada despedir(nombre) que reciba un nombre y muestre un mensaje como:
 #"Adiós, [nombre]. ¡Nos vemos pronto!"
 #Prueba la función con tres nombres diferentes.

def despedir(nombre) :
    print(f"adios  {nombre}" , "hasta luego ")

despedir("juan")
despedir("pipo")
despedir("jose")  

#3. Función con dos parámetros
#Crea una función llamada multiplicar(a, b) que reciba dos números, calcule el producto y lo imprima.

def multiplicar(a , b):
    resultado = a * b 
    print(f"el resultado es : {resultado}")
multiplicar(4,5)    

#4. Función con retorno de valor
 #Crea una función llamada elevar_al_cuadrado(numero) que reciba un número, calcule su cuadrado y retorne el resultado.
 #Luego, guarda ese valor en una variable y muéstralo por pantalla.

def elevar_al_cuadrado(numero):
   cuadrado = numero*numero
   return cuadrado


resultado=elevar_al_cuadrado(4)
print(f"el cuadrado es  : {resultado}")




#  5. Función que use otra función
# Usando la función del ejercicio anterior (elevar_al_cuadrado),
#  crea otra función llamada mostrar_cuadrado(numero)
#  que use la función anterior para obtener el cuadrado y luego imprima el mensaje:
# "El cuadrado de [numero] es [resultado]". 

def mostrar_cuadrado(numero):
    resultado = elevar_al_cuadrado(numero)
    print(f"el cuadrado de : {numero} es : {resultado}")
    
mostrar_cuadrado(5)

#6. Función con parámetros por teclado
# Crea una función llamada saludo_personalizado()
#  que no reciba parámetros, pero que pida el nombre del usuario con input()
#  y luego muestre un saludo con ese nombre.

def saludo_personalizado():
    nombre=(input("ingrese su nombre : "))
    print(f" hola como estas hoy {nombre}")

saludo_personalizado()   


#7. Función que retorne más de un valor
# Define una función llamada operaciones(a, b)
#  que devuelva la suma y la resta de esos dos números.
# Luego, muestra los resultados así:
#suma, resta = operaciones(10, 5)
#print("Suma:", suma)
#print("Resta:", resta)

def operaciones(a, b):
    suma = a + b 
    resta = a - b
    return suma , resta
    
suma , resta = operaciones(4,9)

print(f"la suma es : {suma}")
print(f"la resta es {resta}")

#8. Función que combine lógica simple
# Crea una función llamada es_par(numero)
#  que retorne True si el número es par y False si es impar.
# Luego, usa esa función en un programa que pida un número y 
# diga por pantalla si es par o impar.

def es_par(numero):
    if numero % 2 == 0 :
        return True 
    else : 
        False

# Programa principal
num = int(input("Ingrese un número: "))

if es_par(num):
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")

