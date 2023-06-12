x = int(input("Ingrese la 1ra hora (en formato de 24 horas): "))
y = int(input("Ingrese la 2da hora (en formato de 24 horas): "))

for x in range (x, y):
    for y in range (60):
        for z in range (60):
            format = "{0:02d}:{1:02d}:{2:02d}"
            print(format.format(x, y, z))