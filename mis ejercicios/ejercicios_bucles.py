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
# contador = 1
# while contador <11:
#     print(contador)
#     contador +=1
#     if contador ==6:
#         print("Bucle interrumpido en el número 6")
#         break

"""
Ejercicios for:
"""
"""
Crea una lista llamada animales que contenga tres nombres de animales.
Luego, usa un bucle for para recorrer la lista e imprimir cada uno en pantalla.
"""
# animales = ["mono", "burro", "gato"]
# for animal in animales:
#     print(animal)
"""
Utiliza range() para mostrar los números del 1 al 10, ambos inclusive,
 usando un bucle for y el formato de impresión:
 El número es: X.
"""
# for num in range(1, 11):
#     print(f"El número es: {num}")
"""
Crea una cadena de texto con tu nombre y usa un bucle for para recorrerla,
mostrando cada letra por separado en una nueva línea.
"""
# cadena = "Sandra Divasson"
# for caracter in cadena:
#     print(caracter)
"""
Usando range(), realiza un bucle for que muestre las siguientes líneas:
Iteración número: 0 
Iteración número: 1 
Iteración número: 2 
Iteración número: 3 
Iteración número: 4
Pista: el bucle debe repetirse cinco veces.
"""
for i in range(5):
    print(f"Iteración número: {i}")