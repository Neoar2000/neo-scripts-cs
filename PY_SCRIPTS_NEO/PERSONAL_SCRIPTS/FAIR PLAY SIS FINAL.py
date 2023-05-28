import sqlite3
import time
import datetime

contador_comprobantes = 1

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
    contador_intentos = 0

    while contador_intentos < 4:
        usr = input("\nIntroduce el nombre de usuario: ")
        time.sleep(1)
        pwd = input("\nIntroduce la contraseña: ")

        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()

        # Verificar las credenciales de inicio de sesión en la base de datos
        c.execute("SELECT * FROM usuarios WHERE nombre_usuario=? AND contraseña=?", (usr, pwd))
        if c.fetchone():
            time.sleep(1)
            print("\n¡Has iniciado sesión correctamente!")
            return True
        else:
            contador_intentos += 1
            time.sleep(1)
            print("\nUsuario y/o contraseña incorrecta. Intente nuevamente.")
            time.sleep(1)

    print("\nUsuario BLOQUEADO por exceso de intentos repetidos.\n")
    exit()

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
while not inicio_sesion_exitoso:
    print("Bienvenido al Sistema de Ventas de Fair Play!\n")
    print("(1) Iniciar sesión")
    print("(2) Registrarse")
    print("(3) Salir del Sistema")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        time.sleep(1)
        if login():
            inicio_sesion_exitoso = True
            fecha_valida = False
            while not fecha_valida:
                time.sleep(1)
                fecha = input("\nIntroduce la fecha (dd/mm/yyyy): ")
                if validar_fecha(fecha):
                    fecha_valida = True
                    fecha_guardada = fecha[:6] + str(int(fecha[6:]))
                    time.sleep(1)
                    print("\n¡Fecha validada con éxito!")
                    time.sleep(1)
                    print("\nFecha registrada:", fecha_guardada)
                else:
                    time.sleep(1)
                    print("\nFecha incorrecta. Intente nuevamente.")

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

            # Este es el diccionario para la lista interactiva para el sistema (Menu de opciones)
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
                    print("\nGracias por usar el sistema de ventas de Fair Play. Hasta pronto!\n")
                    time.sleep(1)
                    exit()
                elif opcion in productos:
                    productos_seleccionados = []
                    continuar_seleccionando = True
                    
                    total_compra = 0
                
                    while continuar_seleccionando:
                        producto_seleccionado = productos[str(opcion)]
                        producto_seleccionado["opcion"] = str(opcion)
                        nombre_producto = producto_seleccionado["nombre"]
                        precio_producto = producto_seleccionado["precio"]
                        fecha_venta = fecha_guardada

                        print(f"\nHas seleccionado: {nombre_producto} - Precio: Bs. {precio_producto}\n")
                        productos_seleccionados.append(producto_seleccionado)

                        # Solicitar la cantidad de unidades del último producto seleccionado
                        cantidad_valida = False
                        while not cantidad_valida:
                            try:
                                time.sleep(1)
                                cantidad_producto = input(f"Ingrese la cantidad de unidades que desea comprar de {nombre_producto} (debe ser entre 1 y 5): ").strip()
                                time.sleep(1)
                                if len(cantidad_producto) == 1 and cantidad_producto.isdigit() and int(cantidad_producto) >= 1 and int(cantidad_producto) <= 5:
                                    cantidad_valida = True
                                else:
                                    print("\nCantidad no válida. Por favor, ingrese una cantidad entre 1 y 5 (sin ceros adicionales).\n")
                            except ValueError:
                                time.sleep(1)
                                print("\nEntrada no válida. Por favor, ingrese un número entero.\n")

                        cantidad_producto = int(cantidad_producto)
                        producto_seleccionado["cantidad"] = cantidad_producto
                        total_producto = precio_producto * cantidad_producto
                        total_compra += total_producto

                        # Función para preguntar si se desea agregar más productos
                        opcion_continuar = input("\n¿Desea añadir más productos? (s/n): ")
                        while opcion_continuar.lower() != "s" and opcion_continuar.lower() != "n":
                            time.sleep(1)
                            print("\nOpción no válida. Por favor, ingrese 's' para sí o 'n' para no.")
                            time.sleep(1)
                            opcion_continuar = input("\n¿Desea añadir más productos? (s/n): ")

                        if opcion_continuar.lower() != "s":
                            continuar_seleccionando = False
                        else:
                            # Obtén la opción seleccionada por el usuario
                            opcion_valida = False
                            while not opcion_valida:
                                time.sleep(1)
                                mostrar_menu()
                                opcion = input("\nIngrese el número de opción que desea comprar: ")
                                time.sleep(1)
                                if opcion == "*":
                                    opcion_valida = True
                                    print("\nGracias por usar el sistema de ventas de Fair Play. Hasta pronto!\n")
                                    time.sleep(1)
                                    exit()
                                else:
                                    try:
                                        opcion = int(opcion)
                                        if opcion >= 1 and opcion <= len(productos):
                                            opcion_valida = True
                                        else:
                                            print("\nOpción inválida. Por favor, selecciona una opción válida de la lista de productos.")
                                    except ValueError:
                                        print("\nOpción inválida. Por favor, selecciona una opción válida de la lista de productos.")

                            if opcion != "*":
                                # Continuar con el siguiente producto seleccionado
                                continue

                    # Registrar la venta en el sistema
                    time.sleep(1)
                    print("\nCompra registrada con exito!\n")
                    time.sleep(1)
                    print(f"Total de la compra: Bs. {total_compra:.2f}\n")

                    # Continuar con el siguiente paso (solicitud de NIT/CI)
                    nit_ci_valido = False
                    while not nit_ci_valido:
                        time.sleep(1)
                        nit_ci = input("Ingrese su NIT/CI (solo números, guion y las letras EGD), o ingrese 0 si no tiene NIT: ")
                        nit_ci = nit_ci.strip()  # Eliminar espacios en blanco al inicio y al final
                        time.sleep(1)

                        if nit_ci == "0":
                            nit_ci_valido = True
                        elif len(nit_ci) > 0 and len(nit_ci) <= 10 and all(char.isdigit() or char in "-EGD" for char in nit_ci):
                            nit_ci_valido = True
                        else:
                            print("\nEl formato del NIT/CI no cumple con los requisitos, por favor revise sus datos.\n")

                    print("\nNIT/CI válido:", nit_ci)

                    # Solicitar nombre del beneficiario si no ingresó 0 en el NIT/CI
                    time.sleep(1)
                    if nit_ci == "0":
                        beneficiario = "S/N"
                    else:
                        nombre_valido = False
                        while not nombre_valido:
                            beneficiario = input("\nIngrese el nombre del beneficiario (solo letras): ")
                            time.sleep(1)

                            if beneficiario.isalpha() and len(beneficiario) <= 50:
                                nombre_valido = True
                            else:
                                print("\nEl nombre del beneficiario no cumple con los requisitos. Por favor, ingrese solo letras y no más de 50 caracteres.")
                                time.sleep(1)

                    print("\nNombre del beneficiario: ", beneficiario)


                    # Solicitar método de pago (tarjeta o efectivo)
                    metodo_pago_valido = False
                    while not metodo_pago_valido:
                            time.sleep(1)
                            metodo_pago = input("\nSeleccione el método de pago (tarjeta/efectivo): ")
                            if metodo_pago.lower() == "tarjeta" or metodo_pago.lower() == "efectivo":
                                metodo_pago_valido = True
                            else:
                                time.sleep(1)
                                print("\nOpción no válida. Por favor, ingrese 'tarjeta' o 'efectivo'.")

                    if metodo_pago.lower() == "efectivo":
                        monto_pagado_valido = False
                        while not monto_pagado_valido:
                            time.sleep(1)
                            try:
                                monto_pagado = float(input("\nIngrese el monto pagado por el cliente: "))
                                time.sleep(1)
                                if monto_pagado >= total_compra:
                                    monto_pagado_valido = True
                                    cambio = monto_pagado - total_compra
                                    print("\nCambio a entregar al cliente:", cambio, "\n")
                                else:
                                    print("\nMonto no válido. El monto pagado debe ser igual o mayor al total de la compra.")
                            except ValueError:
                                time.sleep(1)
                                print("\nEntrada no válida. Por favor, ingrese un número válido.")

                        # Generar comprobante
                        time.sleep(1)
                        print("\nGenerando comprobante...")
                        time.sleep(1)
                        print("\n---------------------------------------------------------")
                        print("                        FAIR PLAY")
                        print("                 Comprobante de Ingresos")
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
                        time.sleep(1)

                    elif metodo_pago.lower() == "tarjeta":
                        monto_pagado_valido = False
                        while not monto_pagado_valido:
                            time.sleep(1)
                            try:
                                monto_pagado = float(input("\nIngrese el monto pagado por el cliente: "))
                                time.sleep(1)
                                if monto_pagado == total_compra:
                                    monto_pagado_valido = True
                                else:
                                    print("\nMonto no válido. El monto pagado debe ser igual al total de la compra.")
                            except ValueError:
                                time.sleep(1)
                                print("\nEntrada no válida. Por favor, ingrese un número válido.")

                        # Generar comprobante
                        print("\nGenerando comprobante...")
                        time.sleep(1)
                        print("\n---------------------------------------------------------")
                        print("                        FAIR PLAY")
                        print("                 Comprobante de Ingresos")
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
                        time.sleep(1)
                else:
                    print("\nOpción inválida. Por favor, selecciona una opción válida de la lista de productos.\n")
                    time.sleep(1)

            # Main
            while True:
                time.sleep(1)
                mostrar_menu()

                # Obtén la opción seleccionada por el usuario
                opcion_seleccionada = input("\nIngrese el número de opción que desea comprar: ")

                if opcion_seleccionada in productos or opcion_seleccionada == "*":
                    time.sleep(1)
                    procesar_venta(opcion_seleccionada)
                else:
                    time.sleep(1)
                    print("\nOpción inválida. Por favor, selecciona una opción válida de la lista de productos.")

                # Cerrar la conexión a la base de datos al finalizar
                if opcion_seleccionada == "*":
                    time.sleep(1)
                    print("\nGracias por usar el sistema de ventas de Fair Play. Hasta pronto!\n")
                    time.sleep(1)
                    break

    elif opcion == "2":
        time.sleep(1)
        registrar_usuario()
    elif opcion == "3":
        time.sleep(1)
        print("\nGracias por usar el sistema de ventas de Fair Play. Hasta pronto!")
        time.sleep(1)
        break
    else:
        time.sleep(1)
        print("\nOpción inválida. Por favor, selecciona una opción válida.\n")
        time.sleep(1)