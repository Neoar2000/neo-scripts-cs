x = int(input("Ingrese la hora (en formato de 24 horas): "))
y = int(input("Ingrese los minutos: "))

for x in range(x, y):
    for y in range (60):
        for z in range(60):
            print(x, ":", y, ":", z)