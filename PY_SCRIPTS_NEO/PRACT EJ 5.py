n_adultos = int(input("Ingresa el número de adultos: "))
n_ninos = int(input("Ingresa el número de niños menores de 12 años: "))
duracion_tour = int(input("Ingresa la duración del Tour en días: "))

pb = n_adultos * 1250 + n_ninos * 625
subtotal = pb * duracion_tour
iva = subtotal * 0.12
total = subtotal + iva

print("El total a pagar es: ", total, "bolivianos")