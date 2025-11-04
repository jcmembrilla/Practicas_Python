# # Ejercicios de condicionales
# # Ejercicios 6.1
# # Ejercicio 1
# # Pedir la edad del usuario e indicar si es mayor de edad.
# edad = int(input("Por favor, ingrese su edad: "))
# if edad >= 18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")

# # Ejercicio 2
# # Solicitar un número e indicar si es positivo o negativo.
# numero = int(input("Por favor, ingrese un numero: "))
# if numero >= 0:
#     print("El numero es positivo.")
# else:
#     print("El numero es negativo.")

# # Ejercicio 3
# # Pedir un número y decir si es par o impar.
# numero = int(input("Por favor, ingrese un numero: "))
# if numero%2 == 0:
#     print("El numero es par.")
# else:
#     print("El numero es impar.")

# # Ejercicio 4
# # Ingresar la nota de un alumno y mostrar: Excelente / Aprobado / Desaprobado.
# nota = int(input("La nota es: "))
# if nota == 10:
#     print("Excelente.")
# elif nota >= 4 and nota < 10:
#     print("Aprobado.")
# else:
#     print("Desabrobado.")

# # Ejercicio 5
# # Ingresar una contraseña y verificar si es correcta.
# password = "1234"
# passwordInput = input("Ingrese su contraseña: ")
# if passwordInput == password:
#     print("Su contraseña es correcta.")
# else:
#     print("Su contraseña es incorrecta.")

# # Ejercicio 6
# # Comprobar si un usuario se encuentra en el rango etario entre 20 y 30 años.
# edad = int(input("Ingrese su edad: "))
# if edad >= 20 and edad <= 30:
#     print("Su edad esta en el rango permitido.")
# else:
#     print("Su edad esta fuear del rango permitido.")

# # Ejercicio 7
# # Pedir el año de nacimiento y determinar si la persona es mayor de edad.
# year = int(input("Ingrese su año de nacimiento: "))
# currentYear = 2025
# edad = currentYear - year
# if edad >= 18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")

# # Ejercicio 8
# # Verificar si un número ingresado es múltiplo de 5.
# multiplo = int(input("¿Es multiplo de 5? Ingrese un numero: "))
# if multiplo % 5 == 0:
#     print(f"El numero {multiplo} es multiplo de 5.")
# else:
#     print(f"El numero {multiplo} no es multiplo de 5.")

# # Ejercicio 9
# # Pedir dos números e indicar cuál es el mayor o si son iguales.
# print("Ingrese 2 numeros")
# num1 = int(input("El primero: "))
# num2 = int(input("El segundo: "))
# if num1 > num2:
#     print(f"El primer numero: {num1}, es mayor al segundo: {num2}.")
# elif num2 > num1:
#     print(f"El segundo numero: {num2}, es mayor al primero: {num1}.")
# else:
#     print("Los numeros son iguales.")





# # Ejercicios de condicionales
# # Ejercicios 6.2
# # Multiples condicionales
# # Operadores and, or y not.
 
# # Ejercicio 1
# # Ingresar tres números e indicar cuál es el mayor.
# print("Ingrese 3 numeros")
# num1 = int(input("El primero: "))
# num2 = int(input("El segundo: "))
# num3 = int(input("El tercero: "))

# nums = [num1, num2, num3]
# numMax = max(nums)
# print(f"El numero más grande es {numMax}.")

# if num1 > num2 and num1 > num3:
#     print(f"El numero más grande es {num1}.")
# elif num2 > num1 and num2 > num3:
#     print(f"El numero más grande es {num2}.")
# else:
#     print(f"El numero más grande es {num3}.")

# # Ejercicio 2
# # Sistema de acceso con doble validación (usuario y contraseña).
# print("Registro de usuario")
# print("Ingrese su nombre")
# nombre_usuario = input()
# print("Ingrese su email")
# email_usuario = input()
# print("Ingrese su contraseña")
# contraseña_usuario = input()
# estado_login = False

# print("Usuario Registrado!!!")

# print(f"{nombre_usuario} inicie el login de usuario")
# while not estado_login:
#     print("Ingrese su email")
#     email = input()
#     print("Ingrese su contraseña")
#     contraseña = input()
#     if email == email_usuario and contraseña == contraseña_usuario:
#         estado_login = True
#         print(f"{nombre_usuario}, su login fue exitoso.")
#         break
#     else:
#         print(f"{nombre_usuario}, hay un error en los datos. Intente de nuevo.")

# # Ejercicio 3
# # Pedir un número del 1 al 7 e indicar el día
# # de la semana correspondiente.
# print("¿Día de las semana? Ingrese un numero entre 1 y 7 para saber el día: ")
# day = int(input())
# days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# if day > 0 and day <= 7:
#     print(f"El numero {day} corresponde al día {days[day - 1]}")
# else:
#     print(f"El numero {day} esta fuera de rango.")

# # Ejercicio 4
# # Pedir un número al usuario y verificar si es menor que 0 o mayor que 1000.
# num = int(input("Ingrese un numero: "))
# if num < 0 or num > 1000:
#     print("Fuera de rango.")

# # Ejercicio 5
# # Pedir al usuario su nombre y su contraseña.
# #  Permitir el acceso solo si el nombre es “admin” y la contraseña es “1234”.
# user = "admin"
# password = "1234"
# print("Inicie el login de usuario")
# while True:
#     print("Ingrese su nombre de usuario")
#     name = input()
#     print("Ingrese su contraseña")
#     contraseña = input()
#     if name == user and contraseña == password:
#         print("Su login fue exitoso.")
#         break
#     else:
#         print("Hay un error en los datos. Intente de nuevo.")

# Ejercicio 6
# Pedir la temperatura y la humedad. Mostrar “Clima ideal”
# si la temperatura está entre 20 y 30 grados y la humedad es menor al 70%.

# Ejercicio 7
# Solicitar un número y verificar si no está entre 10 y 50 usando not.
numb= int(input("Ingrese un numero: "))
if not(numb > 10 and numb < 50):
    print("")

# Ejercicio 8
# Pedir al usuario tres notas y mostrar si promociona la materia.
# Promociona si el promedio es mayor o igual a 7 y ninguna nota es menor a 4.
