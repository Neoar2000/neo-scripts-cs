x = int(input("Introduzca el valor del primer lado: "))
y = int(input("Introduzca el valor del segundo lado: "))
z = int(input("Introduzca el valor del tercer lado: "))
if x == y and y == z:
    print("Es un triangulo equilatero.")
elif x == y and y!= z:
    print("Es un triangulo isoceles.")
elif x!=y and y!= z:
    print("Es un triangulo escaleno.")