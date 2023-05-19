x = float(input("Introduzca el primer numero: "))
y = float(input("Introduzca el segundo numero: "))
z = float(input("Introduzca el tercer numero: "))

if x + y == z or x + z == y or y + z == x:
    print("iguales")
else:
    print("distintas")