#EJERCICIO 6.1

"""
ejercicio 1

pedir la edad del usuario e indicar si es mayor de edad
"""
"""
edad = int(input("ingrese su edad : "))
if  edad >=18 :
    print ("es mayor de edad")
else :
    print ("es menor de edad")    
"""
"""
ejercicio 2

solicitar un numero e indicar si es positivo o negativo
"""
"""
numero = int(input("ingrese un numero : "))
if numero >= 0 :
    print("el numero es positivo ")
else :
    print("el numero es negativo ")    
"""
"""
ejercicio 3 

pedir un numero e indicar si es par o impar
"""

"""

numero1 = int(input("ingrese un numero : "))
if numero1 % 2 == 0:
    print("el numero es par")
else  :
    print("el numero es impar")  
"""
"""
ejercicio 4

ingresar la nota de un alumno y mostrar:excelente/aprobado/desaprobado
"""
"""
nota = int(input("ingrese la nota : "))
if nota <= 4 :
    print("desaprobado")
elif nota <=7 :
    print("aprobado")
elif nota >=7 :
    print("excelente") 
"""


"""
ejercicio 5

ingresar una contraseña y verificar si es correcta
"""
"""
contraseña =int(input("ingrese contraseña  (1234)  :"))
if contraseña == 1234 :
    print("contraseña correcta")
else :
    print("contraseña incorrecta")    

"""



"""
ejercicio 6

comprobar si un usuario se encuentra en el rango etario entre 20 y 30 años
"""

"""
edad1 = int(input("ingrese edad :  "))
if edad1 >= 20 and edad1 <=30 :
    print("edad etaria correcta")
else :    
    print("edad etaria incorrecta")
"""

"""
ejercicio 7

pedir el año de nacimiento y determinar si la persona es mayor de edad

"""

"""
año_actual = 2025
edad_nacimiento = int(input("ingrese edad de nacimiento : "))
if año_actual - edad_nacimiento >=18 :
    print("eres mayor de edad")
else:
    print("eres menor de edad")
"""

"""
ejercicio 8
verificar si el numero ingresado es multiplo de 5

"""
"""
numero2 =int(input("ingrese un numero : "))
if numero2 % 5 == 0:
    print("es divisible por 5  ")
else :
    print("no es divisible por 5  ")
    
"""
"""

ejercicio 9

pedir dos numeros e indicar cual es el mayor o si son iguales
"""

valor1 = int(input("ingrese un numero : "))
valor2 = int(input("ingrese un numero : "))

if valor1 > valor2 :
    print( "el numero : ", valor1 , " es mayor que : " , valor2 )
elif valor1 < valor2 :
    print( "el numero : ", valor1 , " es menor que : " , valor2 )
else :
    print( "ambos numeros son iguales : " )
