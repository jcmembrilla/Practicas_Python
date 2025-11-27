#Ejercicios While:
"""
1.
 Crea un programa que muestre los números del 0 al 4 utilizando un bucle while.
 Pista: usa una variable llamada contador que comience en 0 y aumente en 1 en cada iteración.
 """
contador = 0

while contador <4:
 contador = contador + 1
 print(contador)

"""
2.
 Escribe un programa que pida al usuario una contraseña y siga pidiéndola mientras no sea igual a "python123".
 Cuando la contraseña sea correcta, muestra el mensaje: "Acceso concedido".
 """

while True:
  contraseña = input("ingresa tu contraseña: ")
  if contraseña == "python123":
   break
print("acceso concedido")



"""
3.
 Crea un programa que utilice un bucle while para sumar los números del 1 al 5.
 Debe mostrar al final: "La suma total es: X", donde X es el resultado de la suma.
"""
suma = 0
numero = 1
while numero <= 5:
    suma += numero
    numero += 1
print("la suma total es :", suma)


"""
4.
 Escribe un programa que comience con un contador en 1 y muestre los números hasta 10,
 pero detenga el bucle con break si el número es igual a 6.
 Muestra un mensaje que diga "Bucle interrumpido en el número 6".
"""
contador = 1

while contador <= 10:
   if contador == 6:
        print("bucle interrumpido en el numero 6")
        break
   print(contador)
   contador += 1

#Ejercicios for:
"""
1.
 Crea una lista llamada animales que contenga tres nombres de animales.
 Luego, usa un bucle for para recorrer la lista e imprimir cada uno en pantalla.
"""

animales = ["gato", "perro","conejo"]
for animal in animales:
   print(animal)

"""
2.
 Utiliza range() para mostrar los números del 1 al 10, ambos inclusive,
 usando un bucle for y el formato de impresión:
 El número es: X.
"""

for numero in range(1,11):
   print("el numero es:", numero)

"""
3.
 Crea una cadena de texto con tu nombre y usa un bucle for para recorrerla,
 mostrando cada letra por separado en una nueva línea.
"""
nombre = "sofia"
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

for interacion in range(5):
   print("interacion numero:", interacion)