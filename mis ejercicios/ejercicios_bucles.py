"""
Ejercicios While:
"""
"""
Crea un programa que muestre los números del 0 al 4 utilizando un bucle while.
 Pista: usa una variable llamada contador que comience en 0 y aumente en 1 en cada iteración.
"""
# numero = 0
# while numero <5:
#     print(numero)
#     numero +=1

"""
Escribe un programa que pida al usuario una contraseña y siga pidiéndola mientras no sea igual a "python123".
 Cuando la contraseña sea correcta, muestra el mensaje: "Acceso concedido".
"""
# contraseña = "python123"
# contraseña_ingresada = input("Ingrese contraseña:")

# while contraseña != contraseña_ingresada :
#     print("Contraseña Incorrecta.")
#     contraseña_ingresada = input("Ingrese nueva contraseña:")
#     if contraseña == contraseña_ingresada:
#         print("Contraseña correcta.")
"""
Crea un programa que utilice un bucle while para sumar los números del 1 al 5.
Debe mostrar al final: "La suma total es: X", donde X es el resultado de la suma.
"""
# num = 1
# suma = 0
# while num <6:
#     num_2 = num
#     suma = suma + num_2
#     num += 1
#     if num == 6: 
#         print(suma)
#         break
"""
 Escribe un programa que comience con un contador en 1 y muestre los números hasta 10,
 pero detenga el bucle con break si el número es igual a 6.
 Muestra un mensaje que diga "Bucle interrumpido en el número 6".
"""
contador = 1
while contador <11:
    print(contador)
    contador +=1
    if contador ==6:
        print("Bucle interrumpido en el número 6")
        break