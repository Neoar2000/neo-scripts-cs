def mcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return mcd(b, a % b)
    
if __name__ == "__main__":
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El maximo comun divisor de los 2 numeros es:", mcd(a, b))