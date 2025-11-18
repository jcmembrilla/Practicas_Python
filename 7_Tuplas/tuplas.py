""" 
¿Qué es una tupla?

Una tupla es una estructura de datos en Python que permite almacenar
varios elementos en una sola variable, de forma ordenada pero inmutable.
Esto significa que una vez creada, no se puede modificar, es decir, no se 
pueden agregar, eliminar ni cambiar sus elementos.

Las tuplas se escriben entre paréntesis ( ), 
mientras que las listas se escriben entre corchetes [ ].

1. ¿En qué se diferencia una tupla de una lista?

La principal diferencia es que:

Las listas son mutables, es decir, se pueden modificar: agregar, eliminar o cambiar elementos.

Las tuplas son inmutables, o sea, no se pueden modificar una vez creadas.

2. ¿Por qué puede ser útil que una tupla sea inmutable?

Porque garantiza que los datos no cambien durante la ejecución del programa.
Esto es útil cuando se necesita proteger información o asegurar que algo se mantenga 
igual, por ejemplo, coordenadas fijas, configuraciones o valores constantes.
Además, su inmutabilidad hace que las tuplas sean más seguras y puedan usarse 
como claves en diccionarios, cosa que las listas no permiten.

3. ¿Qué ventaja tiene una tupla sobre una lista en términos de rendimiento?

Las tuplas son más rápidas que las listas.
Esto se debe a que, al ser inmutables, Python puede optimizar 
su almacenamiento en memoria y acceder a sus elementos más rápidamente.
Por eso se usan cuando se necesita velocidad y estabilidad en datos que no van a cambiar.

Ejemplo de uso:
Si en un programa se usan millones de datos fijos 
(como nombres de países o constantes matemáticas), 
usar tuplas en lugar de listas mejora el rendimiento general.
"""