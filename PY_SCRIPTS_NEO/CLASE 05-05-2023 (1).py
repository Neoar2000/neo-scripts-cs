def factorial(n):
    producto = 1
    for i in range(1, n+1):
        producto *= i
    return producto

if __name__ == "__main__":
    n = int(input("Ingrese un numero: "))
    print("El factorial de", n, "es", factorial(n))