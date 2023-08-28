usr = input("Ingrese su usuario: ")
pwd = input("Ingrese su contraseña: ")


while usr != "neo" or pwd != "123":
    print("Usuario y contraseña incorrectos.")
    usr = input("Ingrese su usuario: ")
    pwd = input("Ingrese su contraseña: ")

print("Bienvenido Neo!")