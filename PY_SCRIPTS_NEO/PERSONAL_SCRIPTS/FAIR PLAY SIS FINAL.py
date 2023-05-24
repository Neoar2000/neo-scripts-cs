import sqlite3
import time
import getpass

# Conectarse a la base de datos o crearla si no existe
conexion = sqlite3.connect("contabilidad.db")
cursor = conexion.cursor()

# Crear la tabla 'ventas' si no existe
cursor.execute("CREATE TABLE IF NOT EXISTS ventas (id INTEGER PRIMARY KEY AUTOINCREMENT, producto TEXT, precio REAL, fecha DATE)")

# Función para crear la tabla de usuarios si no existe
def crear_tabla_usuarios():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nombre_usuario TEXT PRIMARY KEY, contraseña TEXT)''')
    conn.commit()
    conn.close()

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre_usuario = input("\nIntroduce el nombre de usuario: ")
    time.sleep(1)
    contraseña = input("\nIntroduce la contraseña: ")

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    # Verificar si el usuario ya está registrado
    c.execute("SELECT * FROM usuarios WHERE nombre_usuario=?", (nombre_usuario,))
    if c.fetchone():
        time.sleep(1)
        print("\nEl usuario ya está registrado. Por favor, intenta con otro nombre de usuario.\n")
    else:
        c.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre_usuario, contraseña))
        time.sleep(1)
        print("\nUsuario registrado exitosamente.\n")

    conn.commit()
    conn.close()
    time.sleep(1)

# Función para iniciar sesión
def login():
    usr = input("\nIntroduce el nombre de usuario: ")
    time.sleep(1)
    pwd = getpass.getpass("\nIntroduce la contraseña: ")

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    # Verificar las credenciales de inicio de sesión en la base de datos
    c.execute("SELECT * FROM usuarios WHERE nombre_usuario=? AND contraseña=?", (usr, pwd))
    if c.fetchone():
        time.sleep(1)
        print("\n¡Has iniciado sesión correctamente!\n")
        return True
    else:
        time.sleep(1)
        print("\nUsuario y/o contraseña incorrecta. Intente nuevamente.\n")
        time.sleep(1)
        return False

crear_tabla_usuarios()

# Variable de control para determinar si el inicio de sesión fue exitoso
inicio_sesion_exitoso = False

# Menú principal
while not inicio_sesion_exitoso:
    print("Bienvenido a Fair Play!\n")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        time.sleep(1)
        if login():
            inicio_sesion_exitoso = True
            # Diccionario de productos y precios
            productos = {
                "1": {"nombre": "Zapatillas Nike", "precio": 700.00},
                "2": {"nombre": "Zapatillas Adidas", "precio": 450.00},
                "3": {"nombre": "Zapatillas Under Armour", "precio": 500.00},
                "4": {"nombre": "Zapatillas Converse", "precio": 480.00},
                "5": {"nombre": "Zapatillas Vans", "precio": 420.00},
                "6": {"nombre": "Polera Manga corta", "precio": 150.00},
                "7": {"nombre": "Polera Manga larga", "precio": 200.00},
                "8": {"nombre": "Polera Viviri", "precio": 100.00},
                "9": {"nombre": "Buzo de algodón", "precio": 350.00},
                "10": {"nombre": "Buzo de tela sintética", "precio": 300.00},
                "11": {"nombre": "Gorra", "precio": 100.00},
                "12": {"nombre": "Calcetines", "precio": 50.00}
            }

            # Este es el diccionario para la lista interactiva para el sistema (Menu de opciones)
            preguntas = [
                "Lista de productos Fair Play:\n\n(1) Zapatillas Nike (Bs. 700.00)\n(2) Zapatillas Adidas (Bs. 450.00)\n(3) Zapatillas Under Armour (Bs. 500.00)\n(4) Zapatillas Converse (Bs. 480.00)\n(5) Zapatillas Vans (Bs. 420.00)\n(6) Polera Manga corta (Bs. 150.00)\n(7) Polera Manga larga (Bs. 200.00)\n(8) Polera Viviri (Bs. 100.00)\n(9) Buzo de algodón (Bs. 350.00)\n(10) Buzo de tela sintética (Bs. 300.00)\n(11) Gorra (Bs. 100.00)\n(12) Calcetines (Bs. 50.00)\n\n(0) Salir del Sistema"
            ]

            def obtener_fecha_actual():
                fecha_actual = time.strftime("%Y-%m-%d")
                return fecha_actual

            def mostrar_menu():
                for pregunta in preguntas:
                    print(pregunta)

            def procesar_venta(opcion):
                if opcion == "0":
                    print("\nGracias por usar el sistema de Fair Play. Hasta pronto!\n")
                    conexion.close()
                    time.sleep(1)
                    exit()
                elif opcion in productos:
                    producto_seleccionado = productos[opcion]
                    nombre_producto = producto_seleccionado["nombre"]
                    precio_producto = producto_seleccionado["precio"]
                    fecha_venta = obtener_fecha_actual()

                    print(f"\nHas seleccionado: {nombre_producto} - Precio: Bs. {precio_producto}\n")

                    # Registrar la venta en la base de datos
                    cursor.execute("INSERT INTO ventas (producto, precio, fecha) VALUES (?, ?, ?)",
                                (nombre_producto, precio_producto, fecha_venta))
                    conexion.commit()

                    # Realizar acciones adicionales si es necesario
                    time.sleep(1)
                    print("Gracias por su compra, vuelva pronto!\n")
                else:
                    print("\nOpción inválida. Por favor, selecciona una opción válida de la lista de productos.\n")
                    time.sleep(1)

            def mostrar_ventas():
                cursor.execute("SELECT * FROM ventas")
                ventas = cursor.fetchall()

                print("\nLista de ventas realizadas:")
                print("---------------------------")
                for venta in ventas:
                    venta_id = venta[0]
                    producto = venta[1]
                    precio = venta[2]
                    fecha = venta[3]
                    print(f"ID: {venta_id}, Producto: {producto}, Precio: Bs. {precio}, Fecha: {fecha}")
                print("---------------------------\n")

            # Main
            while True:
                time.sleep(1)
                mostrar_menu()

                # Obtén la opción seleccionada por el usuario
                opcion_seleccionada = input("\nIngrese el número de opción que desea comprar o 'mostrar' para ver las ventas: ")

                if opcion_seleccionada == "mostrar":
                    time.sleep(1)
                    mostrar_ventas()
                elif opcion_seleccionada in productos or opcion_seleccionada == "0":
                    time.sleep(1)
                    procesar_venta(opcion_seleccionada)
                else:
                    time.sleep(1)
                    print("\nOpción inválida. Por favor, selecciona una opción válida de la lista de productos.\n")
                    time.sleep(1)

                # Cerrar la conexión a la base de datos al finalizar
                if opcion_seleccionada == "0":
                    time.sleep(1)
                    print("\nGracias por usar el sistema de Fair Play. Hasta pronto!\n")
                    conexion.close()
                    time.sleep(1)
                    break

    elif opcion == "2":
        time.sleep(1)
        registrar_usuario()
    elif opcion == "3":
        time.sleep(1)
        print("\nGracias por usar el sistema de Fair Play. Hasta pronto!")
        time.sleep(1)
        break
    else:
        time.sleep(1)
        print("\nOpción inválida. Por favor, selecciona una opción válida.\n")
        time.sleep(1)