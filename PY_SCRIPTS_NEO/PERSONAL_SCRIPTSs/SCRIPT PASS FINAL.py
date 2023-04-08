import getpass

pwd = getpass.getpass("Ingrese su contraseña: ")

while pwd != "Guitarhero3":
    print("Contraseña incorrecta. Intente nuevamente.")
    pwd = getpass.getpass("Ingrese su contraseña: ")

print("Contraseña correcta. Bienvenido.")