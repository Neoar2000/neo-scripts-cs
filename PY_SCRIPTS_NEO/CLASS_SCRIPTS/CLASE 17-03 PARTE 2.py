numero = int(input("Ingrese un numero: "))
esPrimo = True

for i in range(2, numero // 2):
    if numero % i == 0:
        esPrimo = False
        break
if esPrimo:
    print("Es primo.")
else:
    print("No es primo.")