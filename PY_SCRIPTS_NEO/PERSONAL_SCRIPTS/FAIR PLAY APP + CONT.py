import sqlite3

# Conectarse a la base de datos o crearla si no existe
conexion = sqlite3.connect("contabilidad.db")
cursor = conexion.cursor()

# Crear la tabla 'ventas' si no existe
cursor.execute("CREATE TABLE IF NOT EXISTS ventas (producto TEXT, precio REAL)")
               
#Esta es la funcion de login del sistema (Iniciar Sesion)
def login():
    print("\nBienvenido a Fair Play!\n")
    usr = input("Introduce el nombre de usuario: ")
    pwd = input("Introduce la contraseña: ")
    while usr != "admin" or pwd != "123":
        print("\nUsuario y/o contraseña incorrecta. Intente nuevamente.\n")
        usr = input("Introduce el nombre de usuario: ")
        pwd = input("Introduce la contraseña: ")
    print("\nContraseña correcta. Bienvenido!\n")

login()

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
    "Lista de productos Fair Play:\n\n(1) Zapatillas Nike\n(2) Zapatillas Adidas\n(3) Zapatillas Under Armour\n(4) Zapatillas Converse\n(5) Zapatillas Vans\n(6) Polera Manga corta\n(7) Polera Manga larga\n(8) Polera Viviri\n(9) Buzo de algodón\n(10) Buzo de tela sintética\n(11) Gorra\n(12) Calcetines\n"
]

for pregunta in preguntas:
    print(pregunta)

# Esta funcion verifica que la opcion seleccionada sea valida, muestra el resultado de la misma y calcula las ganancias totales
def procesar_opcion(opcion):
    producto_seleccionado = productos[opcion]
    nombre_producto = producto_seleccionado["nombre"]
    precio_producto = producto_seleccionado["precio"]
    print(f"\nHas seleccionado: {nombre_producto} - Precio: Bs. {precio_producto}\n")

    # Registrar la venta en la base de datos
    cursor.execute("INSERT INTO ventas VALUES (?, ?)", (nombre_producto, precio_producto))
    conexion.commit()

    # Realizar acciones adicionales si es necesario

while True:
    # Obtén la opción seleccionada por el usuario
    opcion_seleccionada = input("Ingrese el número de opción deseada: ")

    if opcion_seleccionada in productos:
        procesar_opcion(opcion_seleccionada)
        print("\nGracias por su compra, vuelva pronto!\n")
        break
    else:
        print("\nOpción inválida. Por favor, selecciona una opción válida del diccionario de productos.\n")

# Cerrar la conexión a la base de datos al finalizar
conexion.close()