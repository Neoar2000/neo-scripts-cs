numeros = []
while True:
    numero = input("Introduce un número ('fin' para terminar): ")
    if numero == "fin":
        break
    numeros.append(int(numero))

mayor = max(numeros)
menor = min(numeros)

numeros.remove(mayor)
numeros.remove(menor)

print("Lista completa de números:")
print(numeros)