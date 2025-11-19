
def cargar_ventas(nombre_vendedor):
    """Pide al usuario que cargue productos y precios, y devuelve la lista de ventas."""
    ventas = []
    print(f"\n=== CARGA DE PRODUCTOS PARA {nombre_vendedor.upper()} ===\n")

    while True:
        producto = input("Producto vendido: ")
        try:
            precio = float(input("Precio del producto: "))
        except ValueError:
            print(" Ingresá un número válido.\n")
            continue

        ventas.append({"producto": producto, "precio": precio})
        continuar = input("¿Agregar otro producto? (s/n): ").lower()
        if continuar != "s":
            break
        print()

    return ventas


def calcular_total(ventas):
    """Suma los precios de todos los productos vendidos."""
    return sum(p["precio"] for p in ventas)


def mostrar_resultados(vendedor1, vendedor2):
    """Compara las ventas de ambos vendedores y muestra los resultados."""
    total1 = calcular_total(vendedor1)
    total2 = calcular_total(vendedor2)

    print("\n=== RESULTADOS ===")
    print(f"Vendedor 1 vendió {len(vendedor1)} productos por un total de ${total1:.2f}")
    print(f"Vendedor 2 vendió {len(vendedor2)} productos por un total de ${total2:.2f}")

    if total1 > total2:
        print("\n Vendedor 1 fue el que más vendió.")
    elif total2 > total1:
        print("\n Vendedor 2 fue el que más vendió.")
    else:
        print("\n Ambos vendieron lo mismo.")


# --- Programa principal ---
print("=== REGISTRO DE VENTAS ===")

vendedor1 = cargar_ventas("vendedor 1")
vendedor2 = cargar_ventas("vendedor 2")

mostrar_resultados(vendedor1, vendedor2)