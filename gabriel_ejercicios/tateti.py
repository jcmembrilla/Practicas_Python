#matriz = [1,2,3],[4,5,6],[7,8,9]
#print(matriz[0][1])
# Crear tablero con listas
tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Jugador inicial
jugador = "X"
jugadas = 0

while True:
    print("\nTABLERO:")
    for fila in tablero:
        print(fila)

    print(f"\nTurno del jugador: {jugador}")

    # Pedir fila y columna
    fila = int(input("Elegí fila (0, 1, 2): "))
    col = int(input("Elegí columna (0, 1, 2): "))

    # Verificar si está libre
    if tablero[fila][col] != " ":
        print("⚠️ Esa casilla está ocupada. Elegí otra.")
        continue

    # Colocar la X u O
    tablero[fila][col] = jugador
    jugadas += 1

    # ---- Revisar ganador ----
    # Filas
    for f in range(3):
        if tablero[f][0] == tablero[f][1] == tablero[f][2] == jugador:
            print("\nGANÓ EL JUGADOR", jugador)
            for fila in tablero:
                print(fila)
            exit()

    # Columnas
    for c in range(3):
        if tablero[0][c] == tablero[1][c] == tablero[2][c] == jugador:
            print("\nGANÓ EL JUGADOR", jugador)
            for fila in tablero:
                print(fila)
            exit()

    # Diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        print("\nGANÓ EL JUGADOR", jugador)
        for fila in tablero:
            print(fila)
        exit()

    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        print("\nGANÓ EL JUGADOR", jugador)
        for fila in tablero:
            print(fila)
        exit()

    # Empate
    if jugadas == 9:
        print("\nEMPATE")
        for fila in tablero:
            print(fila)
        exit()

    # Cambiar jugador
    jugador = "O" if jugador == "X" else "X"