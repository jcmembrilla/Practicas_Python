# 3 calcular el promedio
nota1 = 9
nota2 = 6
nota3 = 8
promedio = (nota1 + nota2 + nota3) / 3
print(f"Promedio: {promedio}")
# 4 guardar en variables el  precios de tres productos y calcular el total
producto1 = 1000
producto2 = 5000
producto3 = 10000
total = producto1 + producto2 + producto3
print(f"El total de los productos es: {total}.")

# 5 calcular el area de un rectangulo
ladoA = 18
ladoB = 32
totalArea = ladoA * ladoB
print(f"El area de un rectangulo donde sus lados son iguales a {ladoA} y {ladoB} metros es: {totalArea} metros cuadrados")

# 6 convertir de 135 minutos a horas
minutos = 135
aHoras = minutos // 60
resto_minutos = 135 % 60
print(f"Los mintos {minutos} son un total de {aHoras} horas y {resto_minutos} minutos.")

# 7 simular una boleta de un supermercado
productos = [["banana", 3500], ["manzana", 5000], ["cebolla", 1000], ["papa", 1000], ["coca", 3000]]
totalFactura = 0
print("Productos", "Valor")
for key, value in productos:
    print(f"{key}:{" "*15}{value}")
for producto in productos:
    totalFactura += producto[1]

print(f"Total:{" "*15}{totalFactura}")


# 8 comprobar tipos de variables
a = "python" #string
b = 10 #integer
c = 3.14 #float
d = True #boolean
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 9 transformacion de tipos
"""
para transformar a otro tipo le pasamos antes el tipo que queremos que se tranforme.
Ejmeplos:
"""
print(type(int("100"))) #transformamos de string a entero
#para solucionar podriamos hacer:
#print(int("4") + 2) realiza suma
#print("4" + str(2)) concatena