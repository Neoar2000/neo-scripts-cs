numeros = [6, 27, 25, 19, 30, 19, 17, 24, 18, 17]
contador = 0
pos = 0
for i in numeros:
    if i % 3 == 0:
        contador += 1
        print(i, pos)
    pos += 1
print("Hay", contador, "multiplos de 3")
