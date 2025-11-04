lista_supermercado = []
lista_precio =[]

cantidad_productos = int(input("¿Cuantós productos desea ingresar?"))

for i in range(cantidad_productos):
    producto = input("Ingrese nombre del producto:")
    lista_supermercado.append(producto)
    precio = int(input("Ingrese precio del producto "))
    lista_precio.append(precio)

for i in range(cantidad_productos):
    print("--", lista_supermercado[i], "--$", lista_precio[i])

