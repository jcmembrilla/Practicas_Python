"""
Ejercicio 1: Ingresar tres números e indicar cuál es el mayor. 
"""
# num_1 = int(input("Ingrese el primer número: "))
# num_2 = int(input("Ingrese el segundo número: "))
# num_3 = int(input("Ingrese el tercer número: "))

# if num_1 > num_2 and num_1 > num_3:
#     print("El número mayor es:", num_1)
# elif num_2 > num_1 and num_2 > num_3:
#     print("El número mayor es:", num_2)
# elif num_1 == num_2 and num_1 > num_3: 
#     print("El número mayor es:", num_1)
# elif num_1 == num_3 and num_1 > num_2: 
#     print("El número mayor es:", num_1)
# elif num_2 == num_3 and num_2 > num_1: 
#     print("El número mayor es:", num_2)
# elif num_1 == num_2 == num_3:
#     print("Todos los números son iguales: ", num_1)
# else:
#     print("El número mayor es:", num_3)
    
"""
Sistema de acceso con doble validación (usuario y contraseña)
"""


# usuario_ingresado = input("Ingrese su usuario:")
# contraseña_ingresada = int(input("Ingrese su contraseña:"))

# #Sandra
# #1234

# if usuario_ingresado == "sandra" and contraseña_ingresada == 1234:
#     print("Usuario y Contraseña CORRECTOS")
# elif usuario_ingresado != "sandra" and contraseña_ingresada == 1234:
#     print("Usuario INCORRECTO")
# elif usuario_ingresado == "sandra" and contraseña_ingresada != 1234:
#     print("Contrseña INCORRECTA")
# else:
#     print("Usuario y Contraseña INCORRECTOS")


"""
Pedir un número del 1 al 7 e indicar el día de la semana correspondiente.
"""
# dia = int(input("Indique un número del 1 al 7:"))

# if dia == 1:
#     print("LUNES")
# elif dia == 2:
#     print("MARTES")
# elif dia == 3:
#     print("MIERCOLES")
# elif dia == 4:
#     print("JUEVES")
# elif dia == 5:
#     print("VIERNES")
# elif dia == 6:
#     print("SABADO")
# elif dia == 7:
#     print("DOMINGO")
# else: 
#     print("Número ingresado incorrecto.")

"""
Pedir un número al usuario y verificar si es menir que 0 o mayor que 1000
"""
# number = int(input("Ingrese un número que sea menor que cero (0) o mayor que mil (1000): "))

# if number < 0 or number > 1000:
#     print("El número ingresado se encuentra dentro del rango solicitado.")
#     if number < 0:
#         print("El número es menor que 0.")
#     else: 
#         print("El número es mayor que 1000.")
# else:
#     print("El número ingresado no se encuentra dentro del rango solicitado.")

"""
Pedir la temperatura y la humedad. Mostrar "Clima ideal" si la temperatura está ente 20 y 30 grados
y la humedad es menor al 70%
"""
# temperatura = int(input("Ingrese la temperatura: "))
# humedad = int(input("Ingrese la humedad %: "))

# if temperatura >= 20 and temperatura <= 30 and humedad > 70:
#     print("CLIMA IDEAL")
# elif temperatura < 20:
#     print("¡Baja temperatura!")
# else: 
#     print("¡Alta temperatura!")

"""
Solicitar un número y verificar si no esta entre 10 y 50 usando not. 
"""

# num = int(input("Ingrese un número "))

# if  not num >= 10 or num <= 50:
#     print("El número no se encuentra dentro del rango.")
# else:
#     print("El número se encuentra dentro del rango.")

"""
Pedir al usuario tres notas y mostrar si promociona la materia.
Promociona si el promedio es mayor o igual a 7 y ninguna nota es menor a 4.
"""
# nota_1 = int(input("Ingrese la primer nota: "))
# nota_2 = int(input("Ingrese la segunda nota: "))
# nota_3 = int(input("Ingrese la tercera nota: "))

# promedio = (nota_1 + nota_2 + nota_3) / 3

# if nota_1 < 4 or nota_2 < 4 or nota_3 < 4:
#     print("No Promociona.")
# elif promedio >= 7:
#     print("Promociona.")
# else: 
#     print("No promociona.")


