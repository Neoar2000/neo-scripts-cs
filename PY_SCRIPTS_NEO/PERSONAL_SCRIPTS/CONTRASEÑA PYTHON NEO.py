import time
pwd = str(input("Ingrese su contraseña: "))

while pwd != "hola":
    time.sleep(1)
    print("Contraseña incorrecta. Intente de nuevo.")
    pwd = str(input("Ingrese su contraseña: "))

print("Bienvenido de nuevo, Neo!")