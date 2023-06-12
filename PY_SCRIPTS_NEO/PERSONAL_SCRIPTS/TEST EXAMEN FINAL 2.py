# Definir las listas
nombres = []
antiguedades = []
vacaciones = []

# Recopilar los nombres y años de antigüedad de los empleados
for i in range(8):
    nombre = input("Ingrese el nombre del empleado: ")
    antiguedad = int(input("Ingrese los años de antigüedad del empleado: "))
    
    nombres.append(nombre)
    antiguedades.append(antiguedad)
    
    # Calcular la cantidad de días de vacaciones
    if antiguedad <= 5:
        vacaciones.append(15)
    elif antiguedad <= 10:
        vacaciones.append(20)
    else:
        vacaciones.append(25)

# Obtener el nombre del empleado más antiguo
indice_mas_antiguo = antiguedades.index(max(antiguedades))
nombre_mas_antiguo = nombres[indice_mas_antiguo]

# Obtener la cantidad de años de antigüedad del empleado más nuevo
mas_nuevo = min(antiguedades)

# Obtener el promedio de antigüedad de los empleados
promedio_antiguedad = sum(antiguedades) / len(antiguedades)

# Mostrar los resultados
print("El empleado más antiguo es:", nombre_mas_antiguo)
print("La cantidad de años de antigüedad del empleado más nuevo es:", mas_nuevo)
print("El promedio de antigüedad de los empleados es:", promedio_antiguedad)

# Mostrar las tres listas
print("Nombres de empleados:", nombres)
print("Años de antigüedad:", antiguedades)
print("Días de vacaciones:", vacaciones)