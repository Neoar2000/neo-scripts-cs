mensaje = "En el mercho escuchando Ferxxo hoy quiero dormir pero acostado a tu lado."
lista = mensaje.split()
print(lista)

miLista = [45, 100.5, "Hola", True, [5, 4, 3]]
print(len(miLista))

frutas = ["Manzana", "Banana", "Cereza", "Manzana", "Cereza"]
vacia = list()
print(vacia)

lista[2] = "45"
lista[4] = "54"

print(lista[10])

if "Piña" in frutas:
    print("Hay piña casero")
else:
    print("No hay piña casero")

primerLinea = lista[:5]
print(primerLinea)

print(frutas)

frutas.append("Piña")
frutas.append("Sandia")
print(frutas)

cantidadManzana = frutas.count("Manzana")
for i in range(cantidadManzana):
    frutas.remove("Manzana")
print(frutas)

frutas.pop(3)
print(frutas)