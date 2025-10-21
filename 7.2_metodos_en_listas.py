###
# Metodos en listas
###

### Añadir o insertar elementos a listas ###

lista = [1,2,3,4,5]
lista.append(6) #Añade un elemento al final de la lsta
print(lista)

## Insertar un elemento en un pocicion especifica ##

lista2 = ["b", "c", "d"]
print(lista2)
lista2.insert(0, 'a') 
# Inserta una elemento en la poscicon que le indiquemos como primer argumento
#Esto lo que va a hacer es correr todos los elementos una pocicion hacia la derecha
print(lista2)

## Metodo extend ##
#Agrega varios elemntos al final de la lista

lista2.extend(["e", "f"])
print(lista2)

### Eliminar elementos de listas ###

## metodo remove - elimina un elemento a eleccion, pero sol con al primero qu encuentre
lista_eliminar = ["eliminar", "delete", "suprimir", "altf4", "ctr+sup"]
lista_eliminar.remove("delete")
print(lista_eliminar)

## Metodo pop - Predeterminadamente elimina el ultimo elemento de la lista y lo devuelve
lista_eliminar = ["eliminar", "delete", "suprimir", "altf4", "ctr+sup"]
lista_eliminar.pop()
print(lista_eliminar)

#Como lo devuelve podriamos guardarlo en un variable
lista_eliminar = ["eliminar", "delete", "suprimir", "altf4", "ctr+sup"]
ultimo = lista_eliminar.pop()
print("Este es el ultimo elemento de la lista que se acaba de eliminar:",ultimo)
print(lista_eliminar)

#Si a pop le pasamos el indice nos elimina ese elemento
lista_eliminar = ["eliminar", "delete", "suprimir", "altf4", "ctr+sup"]
lista_eliminar.pop(1) #Elimina el segundo elemento de la lista
print(lista_eliminar) #Elimino "delete"

## Metodo del ##

lista_eliminar = ["eliminar", "delete", "suprimir", "altf4", "ctr+sup"]
del lista_eliminar[-1] #Delete ctr+sup
print(lista_eliminar)