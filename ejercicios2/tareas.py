#dni = (45570935, 20807265)

#dni[1] = "saracatunga"

###Ejercicio 2

animales = ("jirafa", "toro", "leon")

print(f"primer animal: {animales[0]}")
print(f"ultimo animal: {animales[2]}")


print("\n lista de animales:")
for zoologico in animales:
    print(f"\n {zoologico}")

###ejercicio 3

animales_lista = list(animales)
animales_lista.append("guanaco")
animales_lista = tuple(animales_lista)

print(animales_lista)