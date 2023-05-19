suma = 0
numList = list()
for i in range (0, 10):
    numList.append(int(input("Ingrese un numero: ")))
for n in numList:
    suma += n
print("El resultado de la suma es:", suma)