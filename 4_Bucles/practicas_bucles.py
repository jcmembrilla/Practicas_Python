"""
5. Función que use otra función
 Usando la función del ejercicio anterior (elevar_al_cuadrado), crea otra función llamada mostrar_cuadrado(numero) que use la función anterior para obtener el cuadrado y luego imprima el mensaje:
 "El cuadrado de [numero] es [resultado]".
"""
def elevar_al_cuadrado(numero):
    return numero **2

def mostrar_cuadrado(numero):
    resultado = elevar_al_cuadrado(numero)
    print(f"El cuadrado de {numero} es {resultado}")

mostrar_cuadrado(8)

