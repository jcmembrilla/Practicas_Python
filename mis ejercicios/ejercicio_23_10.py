#Creo una lista de vendedores
vendedores = ["Ana", "Maria", "Juana", "Josefina"]
#Creo una lista vacia de total de facturado
total_facturado = []
#Voy cargando facturas por vendedor
for i in range(len(vendedores)):
    print("Cargando factura de la vendedora: ", vendedores[i])
    #pregunto cuantas facturas realizó y la guardo en una variable
    facturas_a_cargar = int(input("Indique la cantidad de facturas a cargar: "))
    #declaro variable de factura cargada, y suma_de_facturas
    facturas_cargadas = 0
    suma_de_facturas = 0
    while facturas_cargadas < facturas_a_cargar: 
        monto = float(input("Ingrese monto de factura: "))
        suma_de_facturas = suma_de_facturas + monto
        facturas_cargadas += 1
    
    total_facturado.append(suma_de_facturas)

print(total_facturado)

for i in range(len(total_facturado)):
    maxima_venta = 0
    if total_facturado[i] > maxima_venta:
        vendedora_ganadora= i 

print("La vendedora ganadora es: ", vendedores[vendedora_ganadora])
print("Total facturado $", total_facturado[vendedora_ganadora])
