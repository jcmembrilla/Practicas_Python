"""
Ejercicio 1:
Pedir la edad del usuario e indicar si es mayor de edad.
"""
# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Mayor de edad.")
# else: 
#     print("Menor de edad.")

"""
Solicitar un número e indicar si es positivo o negativo.
"""
# num = int(input("Ingrese un número: "))

# if num > 0:
#     print("NUMERO POSITIVO")
# elif num == 0:
#     print("Su número es 0.")
# else:
#     print("NUMERO NEGATIVO")

"""
Pedir un número e indicar si es par o impar.
"""
# num = int(input("Ingrese un número: "))

# if num % 2 ==0:
#     print("Es PAR.")
# else: 
#     print("Es IMPAR.")

"""
Ingresar la nota de un alumno y mostrar: Excelente /Aprobado/ Desaprobado.
"""
# nota = int(input("Ingrese la nota:"))
# if nota >= 9:
#     print("Excelente")
# elif nota >= 4:
#     print("Aprobado.")
# else: 
#     print("Desaprobado")

"""
Ingresar una contraseña y verificar si es correcta.
"""
# cont = int(input("Ingrese contraseña:"))
# if cont == 123: 
#     print("Contraseña correcta.")
# else: 
#     print("Contraseña incorrecta.")
"""
Comprobar si un usuario se encuentra en el rango etario entre 20 y 30 años.
"""
# edad = int(input("Ingrese su edad:"))
# if edad >= 20 and edad <= 30:
#     print("Rango etario correcto.")
# else:
#     print("Rango etario incorrecto.")

"""
Pedir el año de nacimiento y determinar si la persona es mayor de edad.
"""
# año = int(input("Ingrese año actual: "))
# nac = int(input("Ingrese su año de nacimiento: "))
# edad = año - nac

# if edad >= 18:
#     print ("Eres mayor de edad.")
#     print ("Tienes ", edad, "años.")
# else: 
#     print ("Eres menor de edad")
#     print ("Tienes ", edad, "años.")
"""
Verificar si un número ingresado es múltiplo de 5.
# """
# numero = int(input("Ingrese un número:"))
# resto = numero%5
# if resto == 0:
#     print(f"El número {numero} es multiplo 5.")
# else:
#     print(f"El número {numero} no es multiplo 5.")

"""
Pedir dos números e indicar cuál es el mayor o si son iguales.
"""
numero_1 = int(input("Ingrese un número:"))
numero_2 = int(input("Ingrese otro número:"))

if numero_1 == numero_2:
    print(f"Los números ingresados son iguales. Ingresaste el número {numero_1} dos veces.")
elif numero_1 < numero_2:
    print(f"El {numero_1} es menor que {numero_2}")
else:
    print(f"El {numero_1} es mayor que {numero_2}")