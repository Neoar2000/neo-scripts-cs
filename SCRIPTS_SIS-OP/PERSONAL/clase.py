anio = int(input("Ingrese un anio: "))
if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print("El anio es bisiesto")
else:
    print("El anio no es bisiesto")