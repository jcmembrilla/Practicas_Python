#Creacion de listas
lista1 = [1,2,3,4,5]# Lista de enteros
lista2 = ["Manzanas", "Bananas", "Naranjas", "Uvas"] #Lista de cadenas de texto
lista3 = ["Palabara", 1, 1.12, True] #Lista de tipos mixto

lista_vacia = []

lista_de_listas = [[1,2],[3,4]]


#Acceder a elementos por indice
#Importante recordar el indce 0 es la primera hubicaion, el primero lugar en la lista.
<<<<<<< HEAD:7_listas.py
print(lista2[0]) #El indice cero nos arroja el resultado es manzana
=======
print(lista2[0]) #El indice cero nos arroja el resultado que es manzana
>>>>>>> main:3_Listas/7_listas.py
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
colores = ["azul", "rojo", "naranja", "verde", "amarillo", "violeta", "rosa"]

#Objetivo recortar de 3 a 5
print(colores[2:5])
#Improtante al indice que marcamos primero lo incuye y al ultimo lo excluye
#con esta sintaxis le decimos que recorte a partir 
# del indice 2 (lo incluye) asi que comenzaria por naranja y que 
# recorte hasta el indice 5 (lo excluye) asi que iria hasta amarillo. 

#Si quieres recortar desde el principio dejas el primer valor en blaco
#y dices hasta que ndice quieres
print(colores[:3]) #Resultado los tresprimeros numeros

colores = ["azul", "rojo", "naranja", "verde", "amarillo", "violeta", "rosa"]
#Obter los tres ultimos
print(colores[3:])
#Le indicamos que queremos los ultimos tres numeros dejando en blanco el segundo valor

#Recorrer la lista con el parametro paso
#list[desde:hasta:paso]

lista3 = [1,2,3,4,5,6,7,8]
print(lista3[::2]) #Solo indicamos el tercer parametro para que salte de dos en dos

#Podemos pedir la mima lista de forma inversa, didicando -1 en el tercer parametro
print(lista3[::-1]) #Solo indicamos el tercer parametro para que salte de dos en dos