num1 = int(input("Ingrese el primer numero (debe ser menor que el 2do): "))
num2 = int(input("Ingrese el segundo numero (debe ser mayor que el 1ro): "))
for i in range (num1, num2 + 1):
    if i % 2 != 0:
        print(i)