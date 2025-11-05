"""
ejercicio 4: guardar en variables el precio de tres productos 
y calcular el total.
"""
producto_1 = 50000
producto_2 = 42000
producto_3 = 10000

total = producto_1 + producto_2 + producto_3

print("$", total)


"""
ejercicio 5: calcular el area de un rectangulo.
"""
base = 50
altura = 100
area = base * altura 

print(area, "m2")

"""
ejercicio 6:convertir 135 minutos a horas.
"""
minutos = 135
horas = 60
conversión = minutos / horas
print(conversión, "hs.")


"""
ejercicio 7: simular boleta de supermercado.
"""

nombre_producto_1 = "Leche"
nombre_producto_2 = "Azucar"
nombre_producto_3 = "Chocolate"
nombre_producto_4 = "Yerba"
nombre_producto_5 = "Cafe"

precio_1 = 1500
precio_2 = 1000
precio_3 = 950
precio_4 = 3500
precio_5 = 7000

total_ticket = precio_1 + precio_2 + precio_3 + precio_4 + precio_5

print("#################")
print("    Supermarket   ")
print("#################")
print("")
print(nombre_producto_1, "------", precio_1)
print("")
print(nombre_producto_2, "------", precio_2)
print("")
print(nombre_producto_3, "------", precio_3)
print("")
print(nombre_producto_4, "------", precio_4)
print("")
print(nombre_producto_5, "------", precio_5)
print("")
print("TOTAL --------- $", total_ticket)
print("")
print("#################")
print("GRACIAS POR SU COMPRA")
print("#################")
"""
ejercicio 8: comprobar tipos de variables.

a= 15
b= 3.14 
c= "phyton"
d= False
"""
a = 15
b= 3.14 
c= "phyton"
d= False
print(type(a))
print(type(b))
print(type(c))
print(type(d))

### transformacion de tipos - casting ###
"""
Para transformar a otro tipo le pasamos antes el tipo le pasamos antes 
el tipo que queremos que se transforme.
Ejemplo:
"""
print(type(int("100"))) #Transformamos el string 100 en un entero. 
#print ("4" + 2) #estos dos tipos son diferentes 
#por lo tanto no es posible hacer la operacion ni concatenar,
#arroja un error

# para solucionar podriamos hacer: 
print()