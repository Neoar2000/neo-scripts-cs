categoria = int(input("Introduzca la categoría del paciente (1 a 4): "))
dias = int(input("Introduzca la cantidad de días que ha pasado el paciente en la UTI: "))
edad = int(input("Introduzca la edad del paciente: "))

if categoria == 1:
  costo_base = 1200
elif categoria == 2:
  costo_base = 1500
elif categoria == 3:
  costo_base = 1700
else:
  costo_base = 2000

if edad < 15 or edad > 70:
  costo_adicional = costo_base * 0.2
else:
  costo_adicional = 0

costo_total = (costo_base + costo_adicional) * dias

print("El costo total a ser cancelado es de Bs.", costo_total)