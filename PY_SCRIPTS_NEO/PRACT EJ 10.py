horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de una hora de trabajo: "))

if horas_trabajadas <= 40:
    salario = horas_trabajadas * valor_hora
else:
    horas_normales = 40 * valor_hora
    horas_extras = horas_trabajadas - 40
    
    if horas_extras <= 8:
        salario = horas_normales + (horas_extras * valor_hora * 2)
    else:
        horas_extras_doble = 8 * valor_hora * 2
        horas_extras_triple = (horas_extras - 8) * valor_hora * 3
        salario = horas_normales + horas_extras_doble + horas_extras_triple

print("El salario del trabajador es de: $", salario)