#Creacion de listas
lista1 = [1,2,3,4,5]# Lista de enteros
lista2 = ["Manzans", "Bananas", "Naranjas", "Uvas"] #Lista de cadenas de texto
lista3 = ["Palabara", 1, 1.12, True] #Lista de tipos mixto

lista_vacia = []

lista_de_listas = [[1,2],[3,4]]


#Acceder a elemntos por indice
#Importante recordar el indce 0 es la primera hubicaion, el primero lugar en la lista.
print(lista2[0]) #El indice cero nos arroa el resultado es manzana
print(lista2[1]) #Resulatdo Bananas

#Acceder a las posiciones de forma invertida
print(lista2[-1])#Uvas
print(lista2[-2])#Naranjas

#Acceder a una lista detro de otra lista
#Primero marcamos el nivel para seleccionar a que 
# lista queremos acceder y despues la hubiccion dentro de la lista
print(lista_de_listas[1][0])
#lista_de_listas = [[1,2],[3,4]]
#con 1 le estamos indicando la segunda lista y 
# con 0 la primera hubiccacion el resutado en esta caso es 3

#Slicing, Recorte de listas
lista1 = [1,2,3,4,5,6]

#Objetivo recortar de 3 a 5
print(lista1[2:5])
#con esta sintaxis le decims que re corte a partir 
# del indice 2 asi que comenzaria por el 3 y que 
# recorte hasta el indice 5. Improtante al indice 
# que marcamos primero lo incuye y al ultmo lo excluye

#Si quieres recortar desde el principio dejas el primer valor en blaco
#y dices hasta que ndice quieres
print(lista1[:3]) #Resultado los tresprimeros numeros

lista1 = [1,2,3,4,5,6]
#Obter los tres ultimos
print(lista1[3:])
#Le indicamos que queremos los ultimos tres numeros dejando en blanco el segundo valor

#Recorrer la lista con el parametro paso
#list[desde:hasta:paso]

lista2 = [1,2,3,4,5,6,7,8]
print(lista2[::2]) #Solo indicamos el tercer parametro para que salte de dos en dos

#Podemos pedir la mima lista de forma inversa, didicando -1 en el tercer parametro
print(lista2[::-1]) #Solo indicamos el tercer parametro para que salte de dos en dos


#comentario


