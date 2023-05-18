import time
import sqlite3

conexion = sqlite3.connect('sistema_contable_fp.db')
cursor = conexion.cursor()

# Crear tabla para almacenar las compras y ganancias
cursor.execute('''
    CREATE TABLE IF NOT EXISTS compras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto TEXT,
        precio REAL,
        ganancia REAL
    )
''')
               
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
    {
        "prompt": "Lista de productos Fair Play:\n(1) Zapatillas\n(2) Poleras\n(3) Buzos\n(4) Otros accesorios\n\n(9) Salir del sistema\n\n",
        "opciones": {
            "1": {
                "prompt": "\nHas seleccionado Zapatillas. ¿Qué tipo de zapatillas buscas?\n(1) Deportivas\n(2) Casuales\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                "opciones": {
                    "1": {
                        "prompt": "\nHas seleccionado Zapatillas Deportivas. Estas son nuestras opciones:\n(1) Nike (Bs. 699.99)\n(2) Adidas (Bs. 450.00)\n(3) Under Armour (Bs. 500.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": {
                                "prompt": "\nHas seleccionado Nike (Bs. 699.99). Quieres comprarla?\n(1) Si\n(0) No\n\n",
                                "opciones": {
                                    "1": "\n"
                                }
                            },
                            "2": {
                                "prompt": "\nHas seleccionado Adidas (Bs. 450.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                                "opciones": {
                                    "1": "\n"
                                }
                            },
                            "3": {
                                "prompt": "\nHas seleccionado Under Armour (Bs. 500.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                                "opciones": {
                                    "1": "\n"  
                                }
                            },
                        }
                    },
                },
            },
                    "2": {
                        "prompt": "\nHas seleccionado Zapatillas Casuales. Estas son nuestras opciones:\n(1) Converse (Bs. 480.00)\n(2) Vans (Bs. 420.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": {
                                "prompt": "\nHas seleccionado Converse (Bs. 480.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                                "opciones": {
                                    "1": "\n"
                                }
                            },
                            "2": {
                                "prompt": "\nHas seleccionado Vans (Bs. 420.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                                "opciones": {
                                    "1": "\n"
                                }
                            },
                        }
                    },
            "2": {
                "prompt": "\nHas seleccionado Poleras. Estas son nuestras opciones:\n(1) Manga corta (Bs. 150.00)\n(2) Manga larga (Bs. 200.00)\n(3) Polera Viviri (Bs. 100.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                "opciones": {
                    "1": {
                        "prompt": "\nHas seleccionado Polera Manga corta (Bs. 150.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "\n"
                        }
                    },
                    "2": {
                        "prompt": "\nHas seleccionado Polera Manga larga (Bs. 200.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "\n"  
                        }
                    },
                    "3": {
                        "prompt": "\nHas seleccionado Polera Viviri (Bs. 100.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "\n" 
                        }
                    },
                }
            },
            "3": {
                "prompt": "\nHas seleccionado Buzos. Estas son nuestras opciones:\n(1) De algodon (Bs. 350.00)\n(2) De tela sintetica (Bs. 300.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                "opciones": {
                    "1": {
                        "prompt": "\nHas seleccionado Buzo de algodon (Bs. 350.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "\n" 
                        }
                    },
                    "2": {
                        "prompt": "\nHas seleccionado Buzo de tela sintetica (Bs. 300.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "\n"
                        }
                    },
                }
            },
            "4": {
                "prompt": "\nHas seleccionado Otros accesorios. Estas son nuestras opciones:\n(1) Gorras (Bs. 100.00)\n(2) Calcetines (Bs. 50.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                "opciones": {
                    "1": {
                        "prompt": "\nHas seleccionado Gorras (Bs. 100.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "\n"
                        }
                    },
                    "2": {
                        "prompt": "\nHas seleccionado Calcetines (Bs. 50.00). Quieres comprarla?\n(1) Si\n(0) No\n\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "\n"
                        }
                    },
                }
            },
        }
    }
]

# Esta funcion verifica que la opcion seleccionada sea valida, muestra el resultado de la misma y calcula las ganancias totales
def realizar_pregunta(pregunta, historial=None):
    ganancias_totales = 0
    if historial is None:
        historial = []
        
    prompt = pregunta["prompt"]
    opciones = pregunta["opciones"]
    respuesta = input(prompt)
    
    if respuesta in opciones:
        if isinstance(opciones[respuesta], dict):
            if respuesta == "0":
                if historial:
                    print("\nRegresando al menu anterior...\n")
                    time.sleep(1)
                    realizar_pregunta(historial.pop(), historial)
                else:
                    print("\nNo hay preguntas anteriores.\n")
                    time.sleep(1)
                    realizar_pregunta(pregunta)
            else:
                historial.append(pregunta)
                realizar_pregunta(opciones[respuesta], historial)
        else:
            print(opciones[respuesta])
            if respuesta != "0" and respuesta != "9":
                producto = productos[respuesta]["nombre"]
                precio = productos[respuesta]["precio"]
                ganancia = precio
                ganancias_totales += ganancia

                # Registrar la compra y ganancia en la base de datos
                cursor.execute('INSERT INTO compras (producto, precio, ganancia) VALUES (?, ?, ?)', (producto, precio, ganancia))
                conexion.commit()

                print("Gracias por tu compra de " + producto + ". Vuelve pronto!")
                print("\nGanancias totales: Bs.", ganancias_totales)

    elif respuesta == "0":
        if historial:
            print("\nRegresando al menu anterior...\n")
            time.sleep(1)
            realizar_pregunta(historial.pop(), historial)
        else:
            print("\nNo hay preguntas anteriores.\n")
            time.sleep(1)
            realizar_pregunta(pregunta)
    elif respuesta == "9":
        print("\nAdios! Vuelva pronto!\n")
        conexion.close()
        return
    else:
        print("\nOpción inválida. Por favor, selecciona una opción válida.\n")
        time.sleep(1)
        realizar_pregunta(pregunta, historial)

realizar_pregunta(preguntas[0])