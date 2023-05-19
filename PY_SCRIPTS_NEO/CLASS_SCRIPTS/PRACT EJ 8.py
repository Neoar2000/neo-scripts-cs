n1 = float(input("Introduzca el primer número: "))
n2 = float(input("Introduzca el segundo número: "))

if n1 == n2:
    res = n1 * n2
elif n1 > n2:
    res = n1 - n2
else:
    res = n1 + n2

print("El resultado es:", res)