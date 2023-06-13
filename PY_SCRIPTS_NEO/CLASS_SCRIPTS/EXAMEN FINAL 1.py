numero = input("Ingrese un numero entero que no contenga cero en sus digitos: ")[::-1]

for i in numero:
    print(int(i), int(i) * "*")