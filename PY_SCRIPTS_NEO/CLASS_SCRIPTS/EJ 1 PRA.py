numeros = []
for i in range(10):
    valor = int(input("Introduce un valor numérico: "))
    numeros.append(valor)

numeros.sort()
print("Lista ordenada de menor a mayor:", numeros)

numeros.sort(reverse=True)
print("Lista ordenada de mayor a menor:", numeros)