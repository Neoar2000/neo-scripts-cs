mes = int(input("Introduzca el mes del año, en numeros del 1 al 12: "))
if mes > 12 or mes < 1:
    print("Caracter no valido.")
elif mes == 2:
    print("Este mes tiene 28 dias.")
elif mes % 2 == 0:
    print("Este mes tiene 30 dias.")
elif mes % 2 != 0:
    print("Este mes tiene 31 dias")