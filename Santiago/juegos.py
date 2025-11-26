"""
batalla de datos.
cada jugador tiene dos tiradas
"""


import random

def tirada_de_dados():
    return random.randint(1, 6)

def batalla_de_dados():
    # Tiradas jugador 1
    p1 = tirada_de_dados()
    p2 = tirada_de_dados()
    jugador1 = p1 + p2

    # Tiradas jugador 2
    s1 = tirada_de_dados()
    s2 = tirada_de_dados()
    jugador2 = s1 + s2

    print(f"Jugador 1 sacó: {p1} y {p2} = {jugador1}")
    print(f"Jugador 2 sacó: {s1} y {s2} = {jugador2}")

    if jugador1 > jugador2:
        print("Ganó el jugador 1")
    elif jugador2 > jugador1:
        print("Ganó el jugador 2")
    else:
        print("Empate")

# Ejecutar
batalla_de_dados()
