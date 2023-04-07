numeros = [6, 27, 25, 19, 30, 19, 17, 24, 18, 17]
s = 0
for n in numeros:
    s += n
print(s)

sumaPosPar = 0
for i in range(len(numeros)):
    if i % 2 == 0:
        sumaPosPar+=numeros[i]
print(sumaPosPar)