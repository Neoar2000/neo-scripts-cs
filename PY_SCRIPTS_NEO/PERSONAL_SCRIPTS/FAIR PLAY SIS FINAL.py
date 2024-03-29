import sqlite3
import time
import datetime
import os

# Variable para el contador de comprobantes
contador_comprobantes = 1

# Función para crear la tabla de usuarios si no existe
def crear_tabla_usuarios():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nombre_usuario TEXT PRIMARY KEY, contraseña TEXT)''')
    
    # Crear usuario "admin" con contraseña "12345"
    c.execute("INSERT OR IGNORE INTO usuarios (nombre_usuario, contraseña) VALUES (?, ?)", ("ADMIN", "12345"))

    conn.commit()
    conn.close()

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre_usuario = input("\nIntroduce el nombre de usuario a registrar: ")
    
    contraseña = input("\nIntroduce la contraseña a registrar: ")

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    # Verificar si el usuario ya está registrado
    c.execute("SELECT * FROM usuarios WHERE nombre_usuario=?", (nombre_usuario,))
    if c.fetchone():
        
        print("\nEl usuario ya está registrado. Por favor, intenta con otro nombre de usuario.\n")
    else:
        c.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre_usuario, contraseña))
        
        print("\nUsuario registrado exitosamente.\n")

    conn.commit()
    conn.close()
    

# Función para iniciar sesión
def login():
    contador_intentos = 0

    while contador_intentos < 3:
        usr = input("Introduce el nombre de usuario: ")
        
        pwd = input("\nIntroduce la contraseña: ")

        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()

        # Verificar las credenciales de inicio de sesión en la base de datos
        c.execute("SELECT * FROM usuarios WHERE nombre_usuario=? AND contraseña=?", (usr, pwd))
        if c.fetchone():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡Has iniciado sesión correctamente!")
            return True
        else:
            contador_intentos += 1
            
            if contador_intentos < 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Usuario y/o contraseña incorrecta. Intente nuevamente.\n")
                
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Usuario BLOQUEADO por exceso de intentos repetidos.\n")
    exit()

# Función para validar la fecha ingresada
def validar_fecha(fecha):
    try:
        dia, mes, anio = map(int, fecha.split('/'))
        
        if len(str(anio)) != 4 or str(anio).startswith('0'):
            return False
        
        if ' ' in fecha:
            return False
        
        datetime.datetime(anio, mes, dia)
        return True
    except ValueError:
        return False

crear_tabla_usuarios()

# Variable de control para determinar si el inicio de sesión fue exitoso
inicio_sesion_exitoso = False

# Menú principal
os.system('cls' if os.name == 'nt' else 'clear')
while not inicio_sesion_exitoso:
    
    print("Bienvenido al Sistema de Ventas de Fair Play!\n")
    print("(1) Iniciar sesión")
    print("(2) Registrarse")
    print("(3) Salir del Sistema")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        if login():
            inicio_sesion_exitoso = True
            fecha_valida = False
            while not fecha_valida:

                fecha = input("\nIntroduce la fecha (dd/mm/yyyy): ")
                if validar_fecha(fecha):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    fecha_valida = True
                    fecha_guardada = fecha[:6] + str(int(fecha[6:]))
                    
                    print("\n¡Fecha validada con éxito!")
                    
                    print("\nFecha registrada:", fecha_guardada)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Fecha incorrecta. Intente nuevamente.")

            # Diccionario de productos y precios
            productos = {
                "1": {"nombre": "Puma Polera Active", "precio": 150.00},
                "2": {"nombre": "Polera Nike NP", "precio": 270.00},
                "3": {"nombre": "UA Polera PJT Rock", "precio": 250.00},
                "4": {"nombre": "Zapatilla Deportiva Reebok", "precio": 550.00},
                "5": {"nombre": "Zapatilla Deportiva Puma RBD Game", "precio": 450.00},
                "6": {"nombre": "Sandalia Adidas ZAP Adissage", "precio": 300.00},
                "7": {"nombre": "Sandalia ZAP Adilette Aqua", "precio": 330.00}
            }

            # Esta es la lista interactiva para el sistema (Menu de opciones)
            preguntas = [
                "\nLISTA DE PRODUCTOS A LA VENTA:\n",
            ]

            for clave, producto in productos.items():
                nombre = producto["nombre"]
                precio = producto["precio"]
                pregunta = f"({clave}) {nombre} (Bs. {precio:.2f})"
                preguntas.append(pregunta)

            preguntas.append("\n(*) Salir del Sistema")

            #Funcion para mostrar el menu
            def mostrar_menu():
                for pregunta in preguntas:
                    print(pregunta)

            #Funcion para procesar la venta
            def procesar_venta(opcion):
                global contador_comprobantes
                if opcion == "*":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Gracias por usar el sistema de ventas de Fair Play. Hasta pronto!")
                    
                    exit()
                elif opcion in productos:
                    productos_seleccionados = []
                    continuar_seleccionando = True
                    
                    total_compra = 0
                    # Continuar seleccionando productos hasta que el usuario lo indique
                    while continuar_seleccionando:
                        producto_seleccionado = productos[str(opcion)]
                        producto_seleccionado["opcion"] = str(opcion)
                        nombre_producto = producto_seleccionado["nombre"]
                        precio_producto = producto_seleccionado["precio"]
                        fecha_venta = fecha_guardada

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Has seleccionado: {nombre_producto} - Precio: Bs. {precio_producto}\n")
                        productos_seleccionados.append(producto_seleccionado)

                        # Solicitar la cantidad de unidades del último producto seleccionado
                        cantidad_valida = False
                        while not cantidad_valida:
                            try:
                                
                                cantidad_producto = input(f"Ingrese la cantidad de unidades que desea comprar de {nombre_producto} (debe ser entre 1 y 5): ").strip()
                                
                                if len(cantidad_producto) == 1 and cantidad_producto.isdigit() and int(cantidad_producto) >= 1 and int(cantidad_producto) <= 5:
                                    cantidad_valida = True
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Cantidad no válida. Por favor, ingrese una cantidad entre 1 y 5 (sin ceros adicionales).\n")
                            except ValueError:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("\nEntrada no válida. Por favor, ingrese un número entero.\n")

                        cantidad_producto = int(cantidad_producto)
                        producto_seleccionado["cantidad"] = cantidad_producto
                        total_producto = precio_producto * cantidad_producto
                        total_compra += total_producto

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Total de la compra: Bs. {total_compra:.2f}\n")
                        

                        # Función para preguntar si se desea agregar más productos
                        opcion_continuar = input("¿Desea añadir más productos? (s/n): ")
                        while opcion_continuar.lower() != "s" and opcion_continuar.lower() != "n":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Opción no válida. Por favor, ingrese 's' para sí o 'n' para no.")
                            
                            opcion_continuar = input("\n¿Desea añadir más productos? (s/n): ")

                        if opcion_continuar.lower() != "s":
                            continuar_seleccionando = False
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            # Obtén la opción seleccionada por el usuario
                            opcion_valida = False
                            while not opcion_valida:
                                
                                mostrar_menu()
                                opcion = input("\nIngrese el número de opción que desea comprar: ")
                                
                                if opcion == "*":
                                    opcion_valida = True
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Gracias por usar el sistema de ventas de Fair Play. Hasta pronto!\n")
                                    
                                    exit()
                                else:
                                    try:
                                        opcion = int(opcion)
                                        if opcion >= 1 and opcion <= len(productos):
                                            opcion_valida = True
                                        else:
                                            print("Opción inválida. Por favor, selecciona una opción válida de la lista de productos.")
                                    except ValueError:
                                        print("Opción inválida. Por favor, selecciona una opción válida de la lista de productos.")

                            if opcion != "*":
                                # Continuar con el siguiente producto seleccionado
                                continue

                    # Registrar la venta en el sistema
                    
                    print("Compra registrada con exito!\n")

                   # Continuar con el siguiente paso (solicitud de NIT/CI)
                    nit_ci_valido = False
                    while not nit_ci_valido:
                        nit_ci = input("Ingrese su NIT/CI (solo números, guion y las letras EGD), o ingrese 0 si no tiene NIT: ")
                        nit_ci = nit_ci.strip()

                        if nit_ci == "0":
                            nit_ci_valido = True
                        elif len(nit_ci) > 0 and len(nit_ci.replace("-", "")) > 1 and len(nit_ci.replace("-", "")) <= 10 and all(char.isdigit() or char in "-EGD" for char in nit_ci):
                            nit_ci_valido = True
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("El formato del NIT/CI no cumple con los requisitos, por favor revise sus datos.\n")

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("NIT/CI válido:", nit_ci, "\n")

                    # Solicitar nombre del beneficiario si no ingresó 0 en el NIT/CI
                    if nit_ci == "0":
                        beneficiario = "S/N"
                    else:
                        nombre_valido = False
                        while not nombre_valido:
                            beneficiario = input("Ingrese el nombre del beneficiario (solo letras): ")

                            # Verificar que al menos una palabra contenga letras y cumpla con las demás condiciones
                            if any(word.isalpha() for word in beneficiario.split()) and all(word.isalpha() or word.isspace() for word in beneficiario) and len(beneficiario) <= 50:
                                nombre_valido = True
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("El nombre del beneficiario no cumple con los requisitos. Por favor, ingrese solo letras y no más de 50 caracteres.\n")

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Nombre del beneficiario:", beneficiario, "\n")


                    # Solicitar método de pago (tarjeta o efectivo)
                    metodo_pago_valido = False
                    while not metodo_pago_valido:
                            
                            metodo_pago = input("Seleccione el método de pago (Ponga 't' para tarjeta o 'e' para efectivo): ")
                            if metodo_pago.lower() == "t" or metodo_pago.lower() == "e":
                                metodo_pago_valido = True
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Opción no válida. Por favor, ingrese la opcion correcta.\n")

                    if metodo_pago.lower() == "e":
                        monto_pagado_valido = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        while not monto_pagado_valido:
                            
                            try:
                                
                                print(f"Total de la compra: Bs. {total_compra:.2f}")
                                monto_pagado = float(input("\nIngrese el monto pagado por el cliente: "))
                                
                                if monto_pagado >= total_compra:
                                    monto_pagado_valido = True
                                    cambio = monto_pagado - total_compra
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Cambio a entregar al cliente:", cambio, "\n")
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Monto no válido. El monto pagado debe ser igual o mayor al total de la compra.\n")
                            except ValueError:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Entrada no válida. Por favor, ingrese un número válido.\n")

                        # Generar comprobante
                        print("Generando comprobante...")
                        time.sleep(1)
                        print("\n---------------------------------------------------------")
                        print("                        FAIR PLAY")
                        print("              Comprobante Diario de Ingreso")
                        print("----------------------------------------------------------")
                        print("Fecha:", fecha_venta, "                               CDI-000" + str(contador_comprobantes))
                        print("----------------------------------------------------------")
                        print("Codigo           Detalle                Debe        Haber")
                        print("----------------------------------------------------------")
                        print("11101            Caja                  ", total_compra, "     ")
                        print("11201            Bancos                ")
                        print("21102            Debito Fiscal         ", "           ", total_compra * 0.13)
                        print("51101            Ventas                ", "           ", total_compra * 0.87)
                        print("----------------------------------------------------------")
                        print("                                       ", total_compra, "     ", total_compra)
                        print("\n----------------------------------------------------------")
                        print("Glosa: Por la venta de:\n")
                        for producto in productos_seleccionados:
                            cantidad = producto["cantidad"]
                            nombre = producto["nombre"]
                            print("       -", cantidad, "unidades de", nombre)
                        print("\nal NIT/CI", nit_ci, "a nombre de", beneficiario)
                        print("----------------------------------------------------------")

                        contador_comprobantes += 1
                        

                    elif metodo_pago.lower() == "t":
                        monto_pagado_valido = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        while not monto_pagado_valido:
                            
                            try:
                                
                                print(f"Total de la compra: Bs. {total_compra:.2f}")
                                monto_pagado = float(input("\nIngrese el monto pagado por el cliente: "))
                                
                                if monto_pagado == total_compra:
                                    monto_pagado_valido = True
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Monto no válido. El monto pagado debe ser igual al total de la compra.\n")
                            except ValueError:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Entrada no válida. Por favor, ingrese un número válido.\n")

                        # Generar comprobante
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nGenerando comprobante...")
                        time.sleep(1)
                        print("\n---------------------------------------------------------")
                        print("                        FAIR PLAY")
                        print("              Comprobante Diario de Ingreso")
                        print("----------------------------------------------------------")
                        print("Fecha:", fecha_venta, "                               CDI-000" + str(contador_comprobantes))
                        print("----------------------------------------------------------")
                        print("Codigo           Detalle                Debe        Haber")
                        print("----------------------------------------------------------")
                        print("11101            Caja                  ")
                        print("11201            Bancos                ", total_compra, "     ")
                        print("21102            Debito Fiscal         ", "           ", total_compra * 0.13)
                        print("51101            Ventas                ", "           ", total_compra * 0.87)
                        print("----------------------------------------------------------")
                        print("                                       ", total_compra, "     ", total_compra)
                        print("\n----------------------------------------------------------")
                        print("Glosa: Por la venta de:\n")
                        for producto in productos_seleccionados:
                            cantidad = producto["cantidad"]
                            nombre = producto["nombre"]
                            print("       -", cantidad, "unidades de", nombre)
                        print("\nal NIT/CI", nit_ci, "a nombre de", beneficiario)
                        print("----------------------------------------------------------")

                        contador_comprobantes += 1
                        
                else:
                    print("Opción inválida. Por favor, selecciona una opción válida de la lista de productos.\n")

                input("\n\nPresione ENTER para registrar otra compra...\n")

            # Main
            while True:
                
                mostrar_menu()

                # Obtén la opción seleccionada por el usuario
                opcion_seleccionada = input("\nIngrese el número de opción que desea comprar: ")

                # Verificar si la opción seleccionada es válida
                if opcion_seleccionada in productos or opcion_seleccionada == "*":
                    
                    procesar_venta(opcion_seleccionada)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Opción inválida. Por favor, selecciona una opción válida de la lista de productos.")

                # Cerrar la conexión a la base de datos al finalizar
                if opcion_seleccionada == "*":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Gracias por usar el sistema de ventas de Fair Play. Hasta pronto!\n")
                    
                    break

    elif opcion == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        registrar_usuario()
    elif opcion == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gracias por usar el sistema de ventas de Fair Play. Hasta pronto!")
        
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nOpción inválida. Por favor, selecciona una opción válida.\n")
        