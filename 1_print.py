"""
Print() Es una funcion que utilizamos para 
pintar por consola.
Una funcion es un bloque de codigo que 
creamos para reutilizar ese codigo.
Tambien pueden estar ya creadas como es 
el caso de print()
""" 
nombre = "Ale"
apellido = "Perez"
edad = 25

"""
Ejercicio 1 pintar por consola nombre, apellido y edad.
"""
print("Nombre", nombre, "Apellido", apellido, "Edad", edad )

#Como print es una funcion puede recibir parametros: 
#Estos son sep y end

#Con sep determinamos que queremos que este como
#espacio entre los parametros que recibe
print("perro", "gato", "oso", sep="_")

#Con end determinamos como queremos que se comporte
# el salto de linea. Predeterminadamente da un salto de linea
print("Esto se imprime", end=" ") #Determinamos que end en ves de un salto tenga un espacio
print("en una linea")