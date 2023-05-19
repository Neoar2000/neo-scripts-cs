def factorial(n):
    producto = 1
    for i in range(1, n+1):
        producto *= i
    return producto

def potencia(b, e):
    return b**e

if __name__ == "__main__":
    x = float(input("Ingrese un numero: "))
    b = True
    sen = x

    for i in range (3, 42, 2):
        termino = potencia(x, i)/factorial(i)
        if b:
            sen -= termino
        else:
            sen += termino
        b = not b

    print("El seno de", x, "es:", sen)