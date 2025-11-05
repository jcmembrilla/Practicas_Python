"""
Tipos de datos basicos
-Enteros(int): números sin decimales.
-Decimales(float): números con decimales.
-Cadena de texto(str): texto entre comillas. 
-Booleanos(bool): valores true o false.
"""
#Ejemplo 
print(type(24))
print(type(3.24))
print(type("hola"))
print(type(True))

##Ejercicio 2: Crear una varuable booleana que indique si 
## aprobaste un examen (True/False)

Nota = True

print("¿Aprobaste?")
print(Nota)

###Ejercicio 3: Calcular el promedio de tres calificaciones
"""
Operaciones aritmeticas: 
Operaciones Principales:
(+) suma, (-) resta, (/) division, (*) multiplicacion
(//) division entera, (%) modulo, (**)potencia.
 """


calificacion1 = 7
calificacion2 = 9
calificacion3 = 8

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

print("El promedio es:", promedio)


"""
Entradas datos con Input.
La función Input() permite leer datos que ingresa el usuario por teclado.
ejemplo: nombre = input("Ingresa su nombre:")
"""
### Ejercicio 4: Calcular el promedio de 3 notas que el usuario ingrese por teclado.

calif1 = int(input("Ingrese primera calificación:"))
calif2 = int(input("Ingrese segunda calificación:"))
calif3 = int(input("Ingrese tercera calificación:"))

prom = (calif1 + calif2 + calif3) / 3

print("El promedio es:", prom)
