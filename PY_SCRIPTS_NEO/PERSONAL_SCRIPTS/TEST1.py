numeros = []
while True:
    numero = input("Introduce un número ('fin' para terminar): ")
    if numero == "fin":
        break
    numeros.append(int(numero))

mayor = max(numeros)
mayor_index = numeros.index(mayor)
numeros.remove(mayor)
segundo_mayor = max(numeros)

numeros.insert(mayor_index, mayor)

print("El número mayor es:", mayor)
print("El segundo número mayor es:", segundo_mayor)

print("Lista completa de números:")
print(numeros)
