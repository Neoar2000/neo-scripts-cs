n1 = float(input("Introduzca la primera nota: "))
n2 = float(input("Introduzca la segunda nota: "))
n3 = float(input("Introduzca la tercera nota: "))
n4 = float(input("Introduzca la cuarta nota: "))

nota_eliminada = min(n1, n2, n3, n4)

promedio = (n1 + n2 + n3 + n4 - nota_eliminada) / 3

print("La nota eliminada es:", nota_eliminada)
print("El promedio de practicas del estudiante es:", promedio)