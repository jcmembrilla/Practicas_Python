def presentacion():
    print("El alumno Valentin Ponce asiste al curso de Desarrollo de software")

for presentar in range(3):
   presentacion()

####ejercicio 2

def despedida(Nombre):
    print(f"Adios {Nombre} que tengas lindo día")

for adios in range(3):
   despedida("Valentin")

### Ejercicio 3

def sumar(a, b):
    suma = a + b
    return suma

resultado = sumar(4 ,4)
print(f"El resultado de la cuenta es: {resultado}")

##### Ejercicio 4

def elevar_al_cuadrado(numero):
    elevar = numero**2
    return elevar

resultado2 = elevar_al_cuadrado(6)
print(f"El resultado es: {resultado2}")

#### Ejercicio 5

def mostrar_cuadrado(numero2):
    resultado = elevar_al_cuadrado(numero2)
    print(f"El cuadrado de {numero2} es {resultado}")

mostrar_cuadrado(6)

##### ejercicio 6

def saludo_personalizado():
    nombre = input("Ingrese sus datos aquí: ")
    print(f"bienvenido al sistema {nombre}")

saludo_personalizado()

##### ejercicio 7

def operaciones (a, b):
    suma = a + b
    resta = a - b
    return(suma, resta)

suma, resta = operaciones(10, 5)
print(f"la suma es {suma} y la resta es ")

### ejercicio 8

def es_par(numero):
    if numero %2 == 0:
        print("es par")
    else:
        print("es impar")

numero = int(input("ingrese su numero favorito: "))
es_par(numero)

##### ejercicio 8 con return
##### ejercicio 8 con return
def es_par2(numeroX):
    return numeroX %2 == 0

numeroX = int(input("ingresa un numero: "))
print(es_par2(numeroX))

##ejercicio 9

import random
numero_en_archivo = int(input("ingrese numero del 1 al 10:"))
numero_maquina = random.randint (1, 10)

print(f"la maquina dice:{numero_maquina}")
if numero_maquina == numero_en_archivo:
    print("la maquina gana")
    
else:
    print("tu ganas")