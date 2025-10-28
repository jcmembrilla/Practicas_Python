"""
Tipos de datos basicos
-Enteros(int): numeros sin decimales.
-Decimales(float): nomeros con decimales.
-Cadenas de texto(str): texto entre comillas.
-Booleanos(bool): valores Trues o False
"""
#Ejemplo, con type podemos el tipo de dato.
print("Tipo numerico(int)",type(24))
print("Tipo numerico con decimales(float)",type(3.14))
print("Tipo cadena de texto(str)",type("hola"))
print("Tipo verdader o falso(True/False)",type(True))

""" 
Ejercicio 2: Crear una variable booleana que indique
si aprobaste un examen (True/False)
"""
aprobado = True
print("¿Aprobaste el examen?", aprobado)

"""
Operaciones aritmeticas: Operadores pricipales:
(+) suma, (-) resta, (/) division, (*) multiplicacion
(//) divison entera, (%) modulo, (**) potencia

Ejercicio 3: Calcular el promedio de tres calificaciones
"""
calificacion_1= 7
calificacion_2 = 8
calificacion_3 = 9

promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3
print("El promedio es:", promedio)

"""
Ejercicio 4: Guardar en variables el precio de tres productos 
y calcular el total.
"""
producto1 = 120
producto2 = 85
producto3 = 40

total = producto1 + producto2 + producto3
print("El total de la cmpra es ", total)
"""
Ejercicio 5: Calcular el área de un rectángulo.
"""
base = 40
altura = 60

area = base * altura
print("El area es: ", area)

"""
Ejercicio 6: Convertir 135 minutos a horas.
"""
minutos = 135
horas = minutos // 60

resto= minutos % 60
print(minutos, "minutos equivale a", horas, "horas y", resto, "minutos")

"""
Ejercicio 7: Simular boleta de supermercado.
"""
fideos = 1000
arroz = 1200
pan = 2000

total = fideos + arroz + pan
print("El total es: ", total)

"""
Ejercicio 8: Comprobar tipos de variables.

a = 15
b = 3.14
c = "Python"
d = False
"""
a = 15
b = 3.14
c = "Python"
d = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))




### Transformacion de tipos - casting ###
"""
Para transformar a otro tipo le pasamos 
antes el tipo que queremos que se transforme 
Ejemplos:
"""

print(type(int("100")))#Tranformamos el string 100 en entero.

#print("4" + 2) #estos dos tipos son diferentes 
# por lo tanto no es posible hacer la operacion ni concatenar,
#arroja un error

# para solucionar podriamos hacer:
print(int("5") + 2) #Realizala suma



# tambien
print("4" + str(2)) #Concatena

#print(float("3.34"))#String a float

print(int("3.32"))#String a int


