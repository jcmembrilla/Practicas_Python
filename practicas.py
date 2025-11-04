# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# num = int(input("Ingrese un número: "))

# if es_par(num):
#     print("El número es par.")
# else:
#     print("El número es impar.")


def elevar_al_cuadrado(numero):
    return numero ** 2

def mostrar_cuadrado(numero):
    resultado = elevar_al_cuadrado(numero)
    print(f"El cuadrado de {numero} es {resultado}")

numero_de_usuario = int(input("Ingrese un numero: "))
mostrar_cuadrado(numero_de_usuario)
