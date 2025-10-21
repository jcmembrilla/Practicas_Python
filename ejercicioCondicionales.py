#Ejercicios de condicionales
#Ejercicios 6.1

#Ejercicio 1
#Pedir la edad del usuario e indicar si es mayor de edad.
"""
edad= int(input("Ingrese su edad:"))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")"""

#Ejercicio 2 
#Solicitar un numero e indicar si es positivo o negativo.
"""
solicitarNum= int(input("Ingrese un numero:"))
if solicitarNum > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")"""

#Ejercicio 3
#Pedir un numero y decir si es par o inpar.
"""
solicitarNum= int(input("Ingrese un numero:"))
if solicitarNum % 2 == 0:
    print("El numero es par")
else:
    print("El numero es inpar")"""

#Ejercicio 4
#Ingresar la nota de un alumno y mostrar: Excelente / Aprobado / Desaprobado.
"""nota=int(input("Ingrese su nota:"))
if nota >= 7:
    print("Excelente")
if nota >= 4:
    print("Aprobado") 
else:
    print("Desaprobado")"""

#Ejercicio 5
#Ingresar una contraseña y verificar si es correcta.
"""passwordCorrecto = 123
passwordIngresada = int(input("Ingrese su contraseña numerica :"))
if passwordIngresada == passwordCorrecto:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")"""

#Ejercicio 6
#Comprobar si un usuario se encuentra en el rango etario entre 20 y 30 años.
"""
edad=int(int("Ingrese su edad:"))
if edad >= 20 and edad <= 30:
    print("Usted se encuentra entre 20 y 30 años")
else:
    print("Usted no se encuentra entre 20 y 30 años")"""

#Ejercicio 7
#Pedir el año de nacimiento y determinar si la persona es mayor de edad.
"""
año = int(input("Ingrese su año de nacimiento:"))
if año <= 2007:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")"""

#Ejercicio 8 
#Verificar si un número ingresado es múltiplo de 5.
""""
num = int(input("Ingrese un numero:"))
if num % 5 == 0: 
    print("El numero es multiplo de 5")
else:
    print("El numero no es multiplo de 5")"""

#Ejercicio 9
#Pedir dos números e indicar cuál es el mayor o si son iguales.
"""
num1 = int(input("Ingrese el primer num:"))
num2 = int(input("Ingrese el segundo num:"))
if num1 > num2: 
    print("El num1 es mayor al num2")
elif num2 > num1:
    print("El num2 es mayor al num1")
else:
    print("Los numeros son iguales")
"""

#Ejercicios 6.2
#Multiples condicionales
#Operadores and, or y not.

#Ejercicio 1    
#Ingresar tres números e indicar cuál es el mayor.
"""num1 = int(input("Ingrese el primer num:"))
num2 = int(input("Ingrese el segundo num:"))    
num3 = int(input("Ingrese el tercer num:"))
if num1 > num2 and num1 > num3: 
    print("El num1 es el mayor")
elif num2 > num1 and num2 > num3:
    print("El num2 es el mayor")
elif num3 > num1 and num3 > num2:
    print("El num3 es el mayor")
"""
#Ejercicio 2    
#Sistema de acceso con doble validación (usuario y contraseña).
"""usuario = "Pepito"
contraseña = "1234"

usuarioIngresado = input("Ingrese su usuario:")
contraseñaIngresada = input("Ingrese su contraseña:")

if usuarioIngresado == usuario and contraseñaIngresada == contraseña:
    print("Acceso permitido")
else:
    print("Acceso denegado")"""
"""
#Ejercicio 3
#Pedir un número del 1 al 7 e indicar el día de la semana correspondiente.
pedirNumero = int(input("Ingrese un numero del 1 al 7:"))
if pedirNumero == 1:
    print("Lunes")
elif pedirNumero == 2:
    print("Martes")
elif pedirNumero == 3:
    print("Miercoles")
elif pedirNumero == 4:
    print("Jueves")
elif pedirNumero == 5:
    print("Viernes")
elif pedirNumero == 6:
    print("Sabado")
elif pedirNumero == 7:
    print("Domingo")
else:
    print("El numero ingresado no es valido")
"""
#Ejercicio 4
#Pedir un número al usuario y verificar si es menor que 0 o mayor que 1000.
"""
num = float(input("Ingrese un número: "))

if num < 0 or num > 1000:
    print("El número está fuera del rango (menor que 0 o mayor que 1000).")
else:
    print("El número está dentro del rango.")
    """

#Ejercicio 5
#Pedir al usuario su nombre y su contraseña. Permitir el acceso solo si el nombre es “admin” y la contraseña es “1234”.
"""
nombre = input("Ingrese su nombre: ")
clave = input("Ingrese su contraseña: ")

if nombre == "admin" and clave == "1234":
    print(" Acceso permitido.")
else:
    print(" Acceso denegado.")
"""
#Ejercicio 6
#Pedir la temperatura y la humedad. Mostrar “Clima ideal”. Si la temperatura está entre 20 y 30 grados y la humedad es menor al 70%.
"""
temperatura = float(input("Ingrese la temperatura: "))
humedad = float(input("Ingrese la humedad (%): "))

if 20 <= temperatura <= 30 and humedad < 70:
    print("Clima ideal")
else:
    print(" Clima no ideal")
"""
#Ejercicio 7
#Solicitar un número y verificar si no está entre 10 y 50 usando not.
"""
numero = float(input("Ingrese un número: "))

if not (10 <= numero <= 50):
    print("El número NO está entre 10 y 50.")
else:
    print("El número está entre 10 y 50.")
"""
#Ejercicio 8
#Pedir al usuario tres notas y mostrar si promociona la materia. Promociona si el promedio es mayor o igual a 7 y ninguna nota es menor a 4.
"""
num1 = float(input("Ingrese la primera nota: "))
num2 = float(input("Ingrese la segunda nota: "))
num3 = float(input("Ingrese la tercera nota: "))

promedio = (num1 + num2 + num3) / 3

if promedio >= 7 and num1 >= 4 and num2 >= 4 and num3 >= 4:
    print(f"Promociona con promedio {promedio:.2f}")
else:
    print(f"No promociona. Promedio: {promedio:.2f}")
"""






