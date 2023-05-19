notas = []
for i in range(12):
    nota = int(input(f"Ingrese la calificación del estudiante {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"La media de las notas es: {media:.2f}")

aprobados = 0
reprobados = 0
for nota in notas:
    if nota >= 51:
        aprobados += 1
    else:
        reprobados += 1

porcentaje_aprobados = aprobados / len(notas) * 100
porcentaje_reprobados = reprobados / len(notas) * 100
print(f"Porcentaje de alumnos aprobados: {porcentaje_aprobados:.2f}%")
print(f"Porcentaje de alumnos reprobados: {porcentaje_reprobados:.2f}%")