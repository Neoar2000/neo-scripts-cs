import sqlite3
import time

# Conectarse a la base de datos o crearla si no existe
conexion = sqlite3.connect("contabilidad.db")
cursor = conexion.cursor()

# Crear la tabla 'ventas' si no existe
cursor.execute("CREATE TABLE IF NOT EXISTS ventas (producto TEXT, precio REAL)")

def crear_tabla_usuarios():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nombre_usuario TEXT PRIMARY KEY, contraseña TEXT)''')
    conn.commit()
    conn.close()

def registrar_usuario():
    nombre_usuario = input("\nIntroduce el nombre de usuario: ")
    contraseña = input("\nIntroduce la contraseña: ")

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    # Verificar si el usuario ya está registrado
    c.execute("SELECT * FROM usuarios WHERE nombre_usuario=?", (nombre_usuario,))
    if c.fetchone():
        print("\nEl usuario ya está registrado. Por favor, intenta con otro nombre de usuario.")
    else:
        c.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre_usuario, contraseña))
        print("\nUsuario registrado exitosamente.\n")
        time.sleep(1)

    conn.commit()
    conn.close()

def login():
    usr = input("\nIntroduce el nombre de usuario: ")
    pwd = input("\nIntroduce la contraseña: ")

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    # Verificar las credenciales de inicio de sesión en la base de datos
    c.execute("SELECT * FROM usuarios WHERE nombre_usuario=? AND contraseña=?", (usr, pwd))
    if c.fetchone():
        print("\n¡Has iniciado sesión correctamente!\n")
        return True
    else:
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
        if login():
            inicio_sesion_exitoso = True
            time.sleep(1)
            # Diccionario de productos y precios
            productos = {
                "1": {"nombre": "Zapatillas Nike", "precio": 699.99},
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
                "Lista de productos Fair Play:\n\n(1) Zapatillas Nike\n(2) Zapatillas Adidas\n(3) Zapatillas Under Armour\n(4) Zapatillas Converse\n(5) Zapatillas Vans\n(6) Polera Manga corta\n(7) Polera Manga larga\n(8) Polera Viviri\n(9) Buzo de algodón\n(10) Buzo de tela sintética\n(11) Gorra\n(12) Calcetines\n\n(0) Salir del Sistema"
            ]

            for pregunta in preguntas:
                print(pregunta)

            # Esta funcion verifica que la opcion seleccionada sea valida, muestra el resultado de la misma y calcula las ganancias totales
            def procesar_opcion(opcion):
                if opcion == "0":
                    print("\nGracias por usar el sistema de Fair Play. Hasta pronto!\n")
                    time.sleep(1)
                    exit()
                elif opcion in productos:
                    producto_seleccionado = productos[opcion]
                    nombre_producto = producto_seleccionado["nombre"]
                    precio_producto = producto_seleccionado["precio"]
                    print(f"\nHas seleccionado: {nombre_producto} - Precio: Bs. {precio_producto}\n")

                    # Registrar la venta en la base de datos
                    cursor.execute("INSERT INTO ventas VALUES (?, ?)", (nombre_producto, precio_producto))
                    conexion.commit()

                    # Realizar acciones adicionales si es necesario
                    print("Gracias por su compra, vuelva pronto!\n")
                    time.sleep(1)
                else:
                    print("\nOpción inválida. Por favor, selecciona una opción válida de la lista de productos.\n")
                    time.sleep(1)
                    for pregunta in preguntas:
                        print(pregunta)

            while True:
                # Obtén la opción seleccionada por el usuario
                opcion_seleccionada = input("\nIngrese el número de opción deseada: ")

                if opcion_seleccionada in productos or opcion_seleccionada == "0":
                    procesar_opcion(opcion_seleccionada)
                    break
                else:
                    print("\nOpción inválida. Por favor, selecciona una opción válida de la lista de productos.\n")
                    time.sleep(1)
                    for pregunta in preguntas:
                        print(pregunta)

            # Cerrar la conexión a la base de datos al finalizar
            conexion.close()
            break
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        print("\nGracias por usar el sistema de Fair Play. Hasta pronto!")
        time.sleep(1)
        break
    else:
        print("\nOpción inválida. Por favor, selecciona una opción válida.\n")
        time.sleep(1)