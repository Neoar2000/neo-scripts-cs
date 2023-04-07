sol = int(input("Introduzca el numero de lados del poligono (solo del 3 al 10): "))
if sol == 3:
    print("Es un triangulo")
elif sol == 4:
    print("Es un cuadrado")
elif sol == 5:
    print("Es un pentagono")
elif sol == 6:
    print("Es un hexagono")
elif sol == 7:
    print("Es un heptagono")
elif sol == 8:
    print("Es un octagono")
elif sol == 9:
    print("Es un nonagono")
elif sol == 10:
    print("Es un decagono")
else:
    print("Solo se permiten valores del 3 al 10")