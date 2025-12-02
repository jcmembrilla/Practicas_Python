import random
import copy

matriz = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# para cada ingreso posible, iterar todas sus direcciones y las posibilidades de ganar segun sus posiciones
patrones = {
    (0, 0): [ [(0, 1), (0, 2)], [(1, 0), (2, 0)], [(1, 1), (2, 2)] ],
    (0, 1): [ [(0, 0), (0, 2)], [(1, 1), (2, 1)] ],
    (0, 2): [ [(0, 1), (0, 0)], [(1, 1), (2, 0)], [(1, 2), (2, 2)] ],
    (1, 0): [ [(0, 0), (2, 0)], [(1, 1), (1, 2)] ],
    (1, 1): [ [(1, 0), (1, 2)], [(0, 1), (2, 1)], [(0, 0), (2, 2)], [(0, 2), (2, 0)] ],
    (1, 2): [ [(1, 1), (1, 0)], [(0, 2), (2, 2)] ],
    (2, 0): [ [(1, 0), (0, 0)], [(2, 1), (2, 2)], [(1, 1), (0, 2)] ],
    (2, 1): [ [(2, 0), (2, 2)], [(1, 1), (0, 1)] ],
    (2, 2): [ [(2, 1), (2, 0)], [(1, 2), (0, 2)], [(1, 1), (0, 0)] ]
}

def jugar():
    game = copy.deepcopy(matriz)
    numero_jugadas = 0
    elegir_primero = ""
    elegir_segundo = ""

    nombre_jugador_1 = input("Por favor, ingresar los nombres de los jugadores. \nJugador 1: ")
    nombre_jugador_2 = input("Jugador 2: ")

    print(f"\n1 - {nombre_jugador_1}. 2 - {nombre_jugador_2}")

    # Logica para elgir el turno de los usuarios
    randomplayer = input("Quien comienza? Ingrese el numero 1 o 2 segun el jugador, u oprima Enter para elegirlo aleatoriamente: ")
    # el usuario elige
    if randomplayer == "1":
        elegir_primero = nombre_jugador_1
        elegir_segundo = nombre_jugador_2
        print(f"Empieza {nombre_jugador_1}")
    elif randomplayer == "2":
        elegir_primero = nombre_jugador_2
        elegir_segundo = nombre_jugador_1
        print(f"Empieza {nombre_jugador_2}")
    else:
        # turno de juego random
        pick = elegir_usuario_random()
        if pick == 1:
            elegir_primero = nombre_jugador_1
            elegir_segundo = nombre_jugador_2
            print(f"Empieza {nombre_jugador_1}")
        elif pick == 2:
            elegir_primero = nombre_jugador_2
            elegir_segundo = nombre_jugador_1
            print(f"Empieza {nombre_jugador_2}")

    # loop hasta encontrar ganador
    while True:
        mostrar_matriz(game)

        fila, columna = validar_input(game, elegir_primero, "I")

        numero_jugadas += 1 # sumar hasta que no queden lugares y parar el juego
        if logica_ganador(game, (fila, columna), "I"):
            print(f"******\nEl ganador es I: {elegir_primero}.\n******")
            break
        if numero_jugadas == 9:
            print("******\nFue un empate.\n******")
            break
        mostrar_matriz(game)

        fila, columna = validar_input(game, elegir_segundo, "O")

        numero_jugadas += 1 # sumar hasta que no queden lugares y parar el juego
        if logica_ganador(game, (fila, columna), "O"):
            print(f"El ganador es O: {elegir_segundo}")
            break
    mostrar_matriz(game)

def validar_input(game, usuario, signo):
    # validar el comando del usuario para que funcionen las instrucciones planteadas
    # solo cambiar la matriz si el comando es lo que espera el codigo
    while True:
        jugada = input(f"{usuario} elegir la fila y la columna: ")
        numeros = jugada.split(" ")
        # primera validacion, si existe la fila y la columna
        # segunga validacion, si esta dentro del rango buscado
        # tercera validacion, si la matriz tiene disponible el lugar
        if len(numeros) == 2 and int(numeros[0]) in [0, 1, 2] and int(numeros[1]) in [0, 1, 2]:
            if game[int(numeros[0])][int(numeros[1])] == "-":
                game[int(numeros[0])][int(numeros[1])] = signo
                return int(numeros[0]), int(numeros[1])
            else:
                print("Es un lugar ya ocupado. Ingrese nuevamente otro espacio.")
        else:
            print("El ingreso es incorrecto.")

def elegir_usuario_random():
    return random.randint(1, 2)

def mostrar_matriz(show):
    print("  ", end=" ")
    for i in range(0, 3):
        if i == 2:
            print(f"{i}")
        else:
            print(f"{i}", end="     ")
    for i, line in enumerate(show, start=0):
        print(i, line, sep=" ")

def logica_ganador(game, jugada, sign):
    patron = patrones[jugada] # [[(0, 1), (0, 2)], [(1, 0), (2, 0)], [(1, 1), (2, 2)]]
    ganado = False

    for a, b in patron: # [(0, 1), (0, 2)]
        if game[a[0]][a[1]] == sign and game[b[0]][b[1]] == sign:
            ganado = True
        if ganado:
            break

    return ganado

def mostrar_instruccines():
    print("""
          Cada jugador debera elegir por turnos un espacio en la matriz.
          El ingreso deben ser numeros.
          Primero la fila, despues la columna.
          El primero en lograr una linea de tres signos iguales es el ganador.
          """)


while True:
    print("Bienvenido al TA-TE-TI")
    print("\nMenu")
    print("1 - Jugar")
    print("2 - Instruciones")
    print("3 - Salir")
    orden = input("\nIngresar el numero de la accion para seguir: ")

    if orden == "1":
        jugar()
    elif orden == "2":
        mostrar_instruccines()
    elif orden == "3":
        print("Juego terminado. Gracias por jugar.")
        break