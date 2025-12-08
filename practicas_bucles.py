
"""Ejercicios While: BELEN ANTUNEZ
1.
 Crea un programa que muestre los números del 0 al 4 utilizando un bucle while.
 Pista: usa una variable llamada contador que comience en 0 y aumente en 1 en cada iteración.
"""
contador = 0 
while contador <= 4:
    print(contador)
    contador +=1


"""
2.
 Escribe un programa que pida al usuario una contraseña y siga pidiéndola mientras no sea igual a "python123".
 Cuando la contraseña sea correcta, muestra el mensaje: "Acceso concedido"."""

contraseña = input("Ingrese la contraseña: ")

while contraseña != "python123":
    print(f"Contraseña Incorrecta, intente nuevamente")
    contraseña = input("Ingrese la contraseña: ")

print("Acceso concedido")

"""3.
 Crea un programa que utilice un bucle while para sumar los números del 1 al 5.
 Debe mostrar al final: "La suma total es: X", donde X es el resultado de la suma.
"""
contador = 0
suma = 0
while contador <= 5:
    suma += contador
    contador += 1
    
print(f"La suma total es: {suma}")


"""
4.
 Escribe un programa que comience con un contador en 1 y muestre los números hasta 10,
 pero detenga el bucle con break si el número es igual a 6.
 Muestra un mensaje que diga "Bucle interrumpido en el número 6".
"""
contador = 1
while contador <= 10:
    print(contador)
    if contador == 6:
        print(f"Bucle interrumpido en el número 6")
        break
    contador += 1
 
"""
Ejercicios for:
1.
 Crea una lista llamada animales que contenga tres nombres de animales.
 Luego, usa un bucle for para recorrer la lista e imprimir cada uno en pantalla.
"""

animales = ["lobo", "loro", "Elefante"]
for nombre in animales:
    print(nombre)

"""
2.
 Utiliza range() para mostrar los números del 1 al 10, ambos inclusive,
 usando un bucle for y el formato de impresión: El número es: X.
"""
for num in range(1,11):
    print(f"El numero es: {num}")


"""
3.
 Crea una cadena de texto con tu nombre y usa un bucle for para recorrerla,
 mostrando cada letra por separado en una nueva línea.
"""

nombre = "Belen Antunez"
for letra in nombre:
    print(letra)


"""
4.
 Usando range(), realiza un bucle for que muestre las siguientes líneas:
Iteración número: 0 
Iteración número: 1 
Iteración número: 2 
Iteración número: 3 
Iteración número: 4
Pista: el bucle debe repetirse cinco veces.
"""

for i in range(5):
    print(f"Iteracion numero {i}")