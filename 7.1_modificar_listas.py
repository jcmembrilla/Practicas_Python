#Modificar listas
lista = [1,2,3,4,5,6,7,8]

#Para cambiar un dato indicamos cual es el indice y le asignamos el nuevo valor
lista[0] = 20
print(lista)

### Añadir elemetos a una lista ###

#Forma larga y menos eficiente
lista = lista + [9,10,11]

#Forma recomendada
#Mas corta y eficiente
lista += [12,13,14]
#Des esta forma modificamos directamente la lista

### Sabes la longitud de una lista ###
#Parasaber la logitud lo vamos hacer con la funcion len

lonitud_lista = [1,2,3,4,5,6,7,8,9]
print("La longitus de esta lista es: ", len(lonitud_lista)) #Resultado 9
