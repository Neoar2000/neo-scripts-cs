n = int(input("Ingrese el número de términos que desea generar: "))
a, b = 0, 1
print(a)
print(b)

for i in range(n-2):
    c = a + b
    print(c)
    a, b = b, c