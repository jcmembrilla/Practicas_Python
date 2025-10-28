### Funcion con parametros ###
def saludar_a(nombre): #Declaramos el paramtro
    nombre = (input("ingrese un nombre : "))
    print(f"Hola {nombre}")

saludar_a("nombre")#Le pasamos el argumento que queramos
saludar_a("nombre")
saludar_a("nombre")

#Podemos ver como comienza a tener sentido crear una funcion
#Solo pasandole un argumento se ejecuta el bloque de codigo 
# que preparamos, que ya pensamos y esta esperando que lo usemos.
#Con un solo parametro podemos pasarles diferentes argumentos.
