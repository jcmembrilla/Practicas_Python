
#ejercicio 6.2
#multiples condicionales
#operadores and , or y not
"""

ejercicio 1

ingresar tres numeros e indicar cual es mayor
"""

"""
valor1 = int(input("ingrese un numero : "))
valor2 = int(input("ingrese un numero : "))
valor3 = int(input("ingrese un numero : "))

if valor1 > valor2 and valor1 > valor3:
    print( " el numero : " , valor1 , "es el mayor ") 
elif valor2 > valor1 and valor2 > valor3 :
    print( " el numero : " , valor2 , "es el mayor ")  
elif valor3 > valor1 and valor3 > valor2 :
    print( " el numero : " , valor3 , "es el mayor ")
    
"""


"""
ejercicio 2

sistema de acceso con doble validacion (usuario y contraseña)
"""

"""
usuario = input("ingrese usuario : ") #gabriel
contraseña = input("ingrese contraseña : ") #admind
 
if usuario == "gabriel" and contraseña == "admind" :
    print("acertaste")
else :
    print("sigue intentando")   

"""

"""
ejercicio 3 

pedir un numero del 1 al 7 e indicar el numero de la semana correspondiente
"""

"""
numero_semana = int(input("ingrese numero del 1 al 7  : "))
if numero_semana == 1 :
    print("lunes")
elif numero_semana == 2 :
    print("martes")
elif numero_semana == 3 :
    print("miercoles")     
elif numero_semana == 4 :
    print("jueves")
elif numero_semana == 5 :
    print("viernes")
elif numero_semana == 6 :
    print("sabado")   
elif numero_semana == 7 :
    print("domingo")
else :
    print("numero incorrecto")      

"""


"""
ejercicio 4

pedir un numero al usuario y verificar si es menor que 0 o mayor que 100
"""
"""
valor_nuevo = int(input("ingrese un numero : "))

if valor_nuevo > 0 and valor_nuevo < 100 :
    print("el numero esta en el rango de 0 a 100 ")
else : 
    print("numero fuera de rango")    
"""

"""
ejercicio 5

pedir al usuario su nombre y contraseña 
permitir el acceso solo si el nombre es "admin" y la contraseña "1234"
"""

"""
usuario = input("ingrese usuario : ") #admind
contraseña = int(input("ingrese contraseña : ")) #1234
 
if usuario == "admind" and contraseña == 1234 :
    print("acertaste")
else :
    print("sigue intentando") 

"""


"""
ejercicio 6
pedir la temperatura y la humedad. mostrar "clima ideal"
si la temperatura esta entre 20 y 30 grados y la humedad es menor al 70%
"""

"""
temperatura = int(input("ingrese temperatura : "))
humedad = int(input("ingrese humedad : "))

if temperatura > 20 and temperatura < 30 and humedad < 70 : 
    print(" clima ideal ")
else :
    print("mal clima  ") 
"""

"""
ejercicio 7

solicitar un numero y verificar si no esta esta entre 10 y 50  usando not 
"""

"""
numero_ver = int(input("ingresar numero  :  "))

if not ( numero_ver <= 50 and numero_ver >= 10):
    print(" Número incorrecto")
else:
    print(" Número correcto")

"""


"""
ejercicio 8

pedir al usuario tres notas y mostrar si promociona la materia
promociona si el promedio es mayor  o igual a 7 y ninguna nota es menor a 4 
"""
nota1 = float(input("Ingresá la primera nota: "))
nota2 = float(input("Ingresá la segunda nota: "))
nota3 = float(input("Ingresá la tercera nota: "))

promedio = ( nota1 + nota2 + nota3 ) / 3

if promedio <= 4 :
    print("desaprobado  , " , nota1 , nota2 , nota3 , " tu promedio : " , promedio )
elif promedio < 7 and promedio > 4 :
    print("sigue esforsandote  , " , " tu promedio : " , promedio)    
elif promedio >=  7 :
    print("promociona la materia  , "  , nota1 , nota2 , nota3 , " tu promedio : " , promedio )
else :
    print(promedio)
