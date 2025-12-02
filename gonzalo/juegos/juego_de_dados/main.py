import random

print("Bienvenido al juego de dados!!!")

def jugar():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}.")
    suma_pc = 0
    suma_usuario = 0
    for i in range(1, 3):
        entrada = input(f"Realiza la {i}° tirada con enter o ingresar salir para abandondar: ")
        if entrada == "salir":
            print("Has salido del juego.")
            break
        usuario = tirar_dados()
        pc = tirar_dados()
        print(f"Tu {i}° tirada fue: {usuario}")
        print(f"La tirada de la pc es: {pc}")
        suma_usuario += usuario
        suma_pc += pc
        if i == 2:
            mostrar_resultados(suma_pc, suma_usuario, nombre)

def tirar_dados():
    return random.randint(1, 6)

def mostrar_resultados(suma_pc, suma_usuario, nombre):
    if suma_pc > suma_usuario:
        print(f"La ganadora es la maquina con {suma_pc} puntos. Tu tirada es igual a: {suma_usuario}.")
    elif suma_usuario > suma_pc:
        print(f"Eres el ganador {nombre}!!! Has obtenido {suma_usuario} puntos. Los puntos de la pc son {suma_pc}.")
    else:
        print("Fue un empate.")

    seguir_juego = input(f"Quieres seguir con el juego {nombre}. Si o No: ").lower()
    if seguir_juego == "si":
        menu()
    else:
        print(f"Vuelve cuando quieras {nombre}.")
        
def mostraInstruciones():
    print("Cada jugador realizara dos tiradas de dados.")
    print("La suma mas grande de las 2 tiradas es la ganadora.")
    print("Con el enter seguimos jugando. Si ingresamos salir abandonamos.")

def menu():
    while True:
        print("1 - Jugar.")
        print("2 - Mostrar instrucciones.")
        print("3 - Salir.")
        instruccion = input("Ingrese el numero del menu: ")
        if instruccion == "1":
            jugar()
            break
        elif instruccion == "2":
            mostraInstruciones()
        elif instruccion == "3":
            print("Has salido del juego.")
            break
        else:
            print("Numero incorrecto. El numero debe ser entre 1 y 3.")
menu()