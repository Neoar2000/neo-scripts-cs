num = int(input("Introduzca un numero: "))

if num == 0:
    print("El numero es cero.")
elif num > 0:
    if num % 2 == 0:
        print("El numero es positivo y par.")
    else:
        print("El numero es positivo e impar.")
else:
    if num % 2 == 0:
        print("El numero es negativo y par.")
    else:
        print("El numero es negativo e impar.")