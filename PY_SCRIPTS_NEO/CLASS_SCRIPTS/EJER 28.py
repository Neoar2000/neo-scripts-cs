sum = 0
n = int(input("Introduce una base n: "))
val = input("Introduce un numero: ")
pot = len(val) - 1

for d in val:
    suma = sum + int(d) * n ** pot
    poten = pot - 1

print(suma)