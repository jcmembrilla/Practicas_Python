
# 1. Inmutabilidad:
#Creá una tupla llamada numeros con cinco valores.
#Intentá cambiar el segundo elemento por otro valor y observá el error que aparece.

#numeros = (10, 20, 30, 40, 50)
#print(numeros)
#numeros[1] = 99

#2. Acceso y recorrido:
#Creá una tupla llamada animales con tres nombres de animales.
#a) Mostrá el primer y el último elemento.
#b) Recorrela con un bucle for para imprimir cada animal.

animales = ("perro", "gato", "loro")
print(animales[0])  
print(animales[-1]) 
for animal in animales:
    print(animal)
