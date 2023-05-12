nombres = []
antiguedad = []
vacaciones = []

for i in range(2):
    nom = input("Ingrese nombre: ")
    ant = int(input("Ingrese años de antiguedad: "))
    vac = 0
    if ant < 5:
        vac = 15
    elif ant < 10:
        vac = 20
    else:
        vac = 25
    nombres.append(nom)
    antiguedad.append(ant)
    vacaciones.append(vac)

suma = 0
mayor = 0
menor = 100
posMayor = 0

for i in range(len(nombres)):
    suma += antiguedad[i]
    if antiguedad[i] > mayor:
        mayor = antiguedad[i]
        posMayor = i
    if antiguedad[i] < menor:
        menor = antiguedad[i]

print("El empleado mas antiguo es: ", nombres[posMayor], "con", antiguedad[posMayor], "años de antiguedad")
print("La antiguedad del empleado mas nuevo es: ", menor, "años")
print("El promedio de antiguedad en la empresa es: ", suma/len(nombres))
print(nombres)
print(antiguedad)
print(vacaciones)