def es_par(numero):
    return numero % 2 == 0

numero = int(input("Numero: "))
print("Es par" if es_par(numero) else "Es impar")


