lectura_inicial = float(input("Ingrese la lectura inicial del medidor en kilovatios: "))
lectura_final = float(input("Ingrese la lectura final del medidor en kilovatios: "))

consumo_kwh = lectura_final - lectura_inicial
monto_pago = consumo_kwh * 0.015

aseo_urbano = monto_pago * 0.1
pago_total = monto_pago + aseo_urbano

print("El pago por el consumo en kilovatios es:", monto_pago, "bolivianos")
print("El monto total a pagar es:", pago_total, "bolivianos")