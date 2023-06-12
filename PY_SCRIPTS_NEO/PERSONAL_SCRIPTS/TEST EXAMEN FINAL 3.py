# Función para verificar si los números son múltiplos de 7 consecutivos en orden ascendente
def son_multiplos_consecutivos(n1, n2, n3):
    return n2 == n1 + 7 and n3 == n2 + 7

# Solicitar al usuario los tres múltiplos de 7 consecutivos en orden ascendente
while True:
    num1 = int(input("Ingrese un múltiplo de 7: "))
    num2 = int(input("Ingrese el siguiente múltiplo de 7: "))
    num3 = int(input("Ingrese el último múltiplo de 7: "))

    if son_multiplos_consecutivos(num1, num2, num3):
        break
    else:
        print("Los números ingresados no son múltiplos de 7 consecutivos en orden ascendente. Intente nuevamente.")

print("¡Has ingresado tres múltiplos de 7 consecutivos en orden ascendente!")
print("Los números ingresados son:", num1, num2, "y", num3)