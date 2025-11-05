import random

numero = random.randint(1, 15)

print("Juego adivinanza")

def resultado(valor):
    if numero == valor:
        return True
    else:
        return False
    
def iniciarJuego():
    while True:
        numero_input = int(input("Elija un numero del 1 al 15 y adivine: "))
        if resultado(numero_input):
            print(f"Acertaste. El numero es {numero}.")
            break
        else:
            print("No acertaste.Intente de nuevo")

iniciarJuego()