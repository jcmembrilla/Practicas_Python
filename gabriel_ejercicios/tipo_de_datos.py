"""
tipo de datos basicos
_enteros(int): numeros sin decimales.
_decimales(float): numeros con decimales.
_cadena de textos(str): textos entre comillas.
_booleanos(bool): valores trues o false.

"""
#ejemplo
print("tipo numerico(int)",type(24))
print("tipo con decimales()",type(3.16))
print("tipo cadena de texto(estring)",type("hola"))
print("tipo booleano(bool)",type("true"))

"""
eje 2: crear una variable booleana que indique si aprobaste un examen (false o true)

"""
aprobado=True
desaprobado=False
print("nota ", aprobado)

"""
eje 3 :calcular el promedio de tres calificaciones
operaciones aritmeticas : operadores principales :
(+)suma , (-) resta , (*)multiplicacion , (/) division , (//)division entera , (%)modulo , (**)potencia

"""

nota1=5
nota2=7
nota3=10
promedio=(nota1+nota2+nota3)/3

print(promedio)

"""
entrada de datos con imput
la funcion input (input) permite leer datos que ingresa  el usuario por teclado
ejemplo: nombre = input =("ingrese su nombre)
eje 4: calcular el promedio de 3 notas que el usuario ingrese por teclado
"""

###print("El promedio es:", (int(input("Nota 1: ")) + int(input("Nota 2: ")) + int(input("Nota 3: "))) / 3)

"""
nota1 = int(input("Ingrese su primera nota: "))
nota2 = int(input("Ingrese su segunda nota: "))
nota3 = int(input("Ingrese su tercera nota: "))


promedio = (nota1 + nota2 + nota3) / 3


print("El promedio es:", promedio)

"""
"""
eje 4 :guardar en variables el precio de tres productos y calcular el total.

"""
producto1 = 10
producto2 = 20
producto3 = 30
total = (producto1 + producto2 + producto3)
print ( "el total es  : " , total)

"""
ejer 5: calcular el area de un rectangulo.

"""
base = 10
altura = 20
area = (base * altura)
print("el area es : " , area )

"""
ejer 6: convertir 135 minutos a horas .

"""
minutos = 135
horas =(minutos / 60 )
print ("son : " , horas , "horas"  )
 
"""
ejer 7:  simular boleta de supermercado.

"""
azucar = 300
harina = 400
aceite = 100
tot_super =(azucar +harina + aceite)
print ("precio azucar :" , azucar)
print ("precio harina :" , harina)
print ("precio aceite :" , aceite)
print ("total tiquet : " , tot_super)

""" 
ejer 8: comprobar tipo de variables.  

a = 15
b = 3.14
c = "python"
d = false

"""

a = 15
b = 3.14
c = "python"
d = False

print( type(a) )
print( type(b))
print( type(c))
print( type(d))

###  transformacion de tipos _ casting ###

"""
para transformar a otro tipo le pasamos antes el tipo que queremos que se transforme
ejemplos:


"""
print(type(int("100")))# transformamos el estring 100 en entero.

#print("4" + 2 )# estos dos tipos son diferentes
# por lo tanto no es posible hacer la operacion ni concatenar,
# arroja un error 

#para solucionar podriamos hacer :
print(int("4") + 2 ) # realiza la suma

 # tambien 
print("4" + str(2)) #concatena

print(float("3.34")) #string a float

print(int("3.32")) # string a int
