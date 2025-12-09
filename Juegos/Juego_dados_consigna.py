"""
Batalla de dados.
cada jugador tiene dos tiradas.

Pedir los nombres de los jugadres.

Agregar un menu con tres opciones:
1. Jugar
2. Instrucciones de juego
3. Salir

"""
import random

def tirar_dado():
    return random.randint(1, 6)