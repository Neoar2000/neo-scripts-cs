nombre = input("Introduzca su nombre: ")
while nombre != nombre.isalpha:
    if not nombre.isalpha():
        print("Valor errado. Intente nuevamente")
    else:
        print("Hola " + nombre + "!")