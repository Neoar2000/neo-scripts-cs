estudiantes = {}

for i in range (2): 
    apellidos = input("Ingrese sus dos apellidos separados por un espacio: ")
    calificacion = input("Ingrese su calificacion: ")
    estudiantes[apellidos] = calificacion

mayor_nota = max(estudiantes.values())
mejor_estudiante = [key for key, value in estudiantes.items() if value == mayor_nota][0]
apellido_mejor_estudiante = mejor_estudiante

print("El apellido del mejor estudiante es", apellido_mejor_estudiante)

contador = 0
for key, value in estudiantes.items():
    if value < 51:
        contador += 1
print("La cantidad de estudiantes que reprobaron es", contador)

suma = 0
for key, value in estudiantes.items():
    suma += int(value)
promedio = suma / len(estudiantes)
print("El promedio de las notas de los estudiantes es", promedio)