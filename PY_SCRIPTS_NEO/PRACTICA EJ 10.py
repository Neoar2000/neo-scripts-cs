temps = []
centinela = -999

while True:
    temp = float(input("Ingrese una temperatura (o -999 para salir): "))
    if temp == centinela:
        break
    temps.append(temp)

num_temp_bajo_cero = sum(1 for t in temps if t < 0)
porcentaje_temp_bajo_cero = (num_temp_bajo_cero / len(temps)) * 100
temp_max = max(temps)

print("Porcentaje de temperaturas por debajo de cero grados: {:.2f}%".format(porcentaje_temp_bajo_cero))
print("Temperatura más alta: {:.1f}".format(temp_max))