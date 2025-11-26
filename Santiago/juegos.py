"""
batalla de datos.
cada jugador tiene dos tiradas
"""


import random
def tirada_de_dados():
    random.randint(1, 6)


def batalla_de_dados():
    jugador1 = 0
    
    primera_tirada = tirada_de_dados 
    segunda_tirada = tirada_de_dados 
    
    jugador1 = primera_tirada() + segunda_tirada()
    jugador2 = primera_tirada() + segunda_tirada()

    print( f"{jugador1}")
    print(f"{jugador2}")

    if jugador1 > jugador2:
        print(f"gano {jugador1}")

    elif jugador2 > jugador1:

        print(f"gano {jugador2}")
    else:

        print("empate")


print(batalla_de_dados())