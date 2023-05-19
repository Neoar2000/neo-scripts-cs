# Caso particular:
prestamo = 10000
interes = 0.02

interes_mes = prestamo * interes

print("El interés a pagar por mes es:", interes_mes, "bolivianos")

# Caso general:
prestamo = float(input("Ingrese el monto del préstamo en bolivianos: "))
interes = float(input("Ingrese la tasa de interés mensual como decimal (por ejemplo, 0.02 para el 2%): "))

interes_mes = prestamo * interes

print("El interés a pagar por mes es:", interes_mes, "bolivianos")