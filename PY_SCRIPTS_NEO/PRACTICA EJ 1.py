ft = float(input("Ingresa la cantidad de pies de la distancia: "))
inch = float(input("Ingresa la cantidad de pulgadas de la distancia: "))
ft2inch = ft * 12 + inch
cm = ft2inch * 2.54
print("La distancia de " + str(ft) + " pies y " + str(inch) + " pulgadas son " + str(cm) + " centímetros de distancia.")