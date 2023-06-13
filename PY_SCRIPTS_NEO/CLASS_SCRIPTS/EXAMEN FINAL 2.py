listatext = []
listanum = []

oracion = input("Ingrese una oracion: ")
cortado = oracion.split(" ")
listatext.append(cortado)

for i in cortado:
    listanum.append(len(i))
    
promedio = sum(listanum)/len(listanum)

print(listanum)
print("Promedio:", promedio)