ehum = int(input("Introduzca la edad de su perro en años humanos: "))
if ehum <= 2:
    edog = ehum * 10.5
else:
    edog = 2 * 10.5 + (ehum - 2) * 4
print("El equivalente en edad de perro es: " + str(edog) + " años.")