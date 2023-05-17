from Preguntas import pregunta

usr = input("Introduce el nombre de usuario: ")
pwd = input("Introduce la contraseña: ")

while usr != "admin" or pwd != "123":
    print("\nUsuario y/o contraseña incorrecta. Intente nuevamente.\n")
    usr = input("Introduce el nombre de usuario: ")
    pwd = input("Introduce la contraseña: ")

print("\nContraseña correcta. Bienvenido!\n")

preguntas = [
    {
        "prompt": "Lista de productos Fair Play\n(1) Zapatillas\n(2) Poleras\n(3) Buzos\n(4) Otros accesorios\n\n(9) Salir del sistema\n\n",
        "opciones": {
            "1": {
                "prompt": "Has seleccionado Zapatillas. ¿Qué tipo de zapatillas buscas?\n(1) Deportivas\n(2) Casuales\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                "opciones": {
                    "1": {
                        "prompt": "Has seleccionado Zapatillas Deportivas. Estas son nuestras opciones:\n(1) Nike (Bs. 699.99)\n(2) Adidas (Bs. 450.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": {
                                "prompt": "Has seleccionado Nike (Bs. 699.99). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n\n",
                                "opciones": {
                                    "1": "Gracias por tu compra. Vuelve pronto!",
                                    "2": "Gracias por tu visita. Vuelve pronto!",
                                }
                            },
                            "2": {
                                "prompt": "Has seleccionado Adidas (Bs. 450.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                                "opciones": {
                                    "1": "Gracias por tu compra. Vuelve pronto!",
                                    "2": "Gracias por tu visita. Vuelve pronto!",
                                }
                            }, 
                        }
                    },
                    "2": {
                        "prompt": "Has seleccionado Zapatillas Casuales. Estas son nuestras opciones:\n(1) Converse (Bs. 480.00)\n(2) Vans (Bs. 420.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": {
                                "prompt": "Has seleccionado Converse (Bs. 480.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                                "opciones": {
                                    "1": "Gracias por tu compra. Vuelve pronto!",
                                    "2": "Gracias por tu visita. Vuelve pronto!",
                                }
                            },
                            "2": {
                                "prompt": "Has seleccionado Vans (Bs. 420.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                                "opciones": {
                                    "1": "Gracias por tu compra. Vuelve pronto!",
                                    "2": "Gracias por tu visita. Vuelve pronto!",
                                }
                            },
                            
                        }
                    },
                }
            },
            "2": {
                "prompt": "Has seleccionado Poleras. Estas son nuestras opciones:\n(1) Manga corta (Bs. 150.00)\n(2) Manga larga (Bs. 200.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                "opciones": {
                    "1": {
                        "prompt": "Has seleccionado Polera Manga corta (Bs. 150.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "Gracias por tu compra. Vuelve pronto!",
                            "2": "Gracias por tu visita. Vuelve pronto!",
                        }
                    },
                    "2": {
                        "prompt": "Has seleccionado Polera Manga larga (Bs. 200.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "Gracias por tu compra. Vuelve pronto!",
                            "2": "Gracias por tu visita. Vuelve pronto!",
                        }
                    },
                }
            },
            "3": {
                "prompt": "Has seleccionado Buzos. Estas son nuestras opciones:\n(1) Con capucha (Bs. 350.00)\n(2) Sin capucha (Bs. 300.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                "opciones": {
                    "1": {
                        "prompt": "Has seleccionado Buzo Con capucha (Bs. 350.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "Gracias por tu compra. Vuelve pronto!",
                            "2": "Gracias por tu visita. Vuelve pronto!",
                        }
                    },
                    "2": {
                        "prompt": "Has seleccionado Buzo Sin capucha (Bs. 300.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "Gracias por tu compra. Vuelve pronto!",
                            "2": "Gracias por tu visita. Vuelve pronto!",
                        }
                    },
                }
            },
            "4": {
                "prompt": "Has seleccionado Otros accesorios. Estas son nuestras opciones:\n(1) Gorras (Bs. 100.00)\n(2) Calcetines (Bs. 50.00)\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                "opciones": {
                    "1": {
                        "prompt": "Has seleccionado Gorras (Bs. 100.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "Gracias por tu compra. Vuelve pronto!",
                            "2": "Gracias por tu visita. Vuelve pronto!",
                        }
                    },
                    "2": {
                        "prompt": "Has seleccionado Calcetines (Bs. 50.00). Quieres comprarla?\n(1) Si\n(2) No\n\n(0) Retroceder\n(9) Salir del sistema\n\n",
                        "opciones": {
                            "1": "Gracias por tu compra. Vuelve pronto!",
                            "2": "Gracias por tu visita. Vuelve pronto!",
                        }
                    },
                }
            },
        }
    }
]

def realizar_pregunta(pregunta, historial=None):
    if historial is None:
        historial = []
        
    prompt = pregunta["prompt"]
    opciones = pregunta["opciones"]
    respuesta = input(prompt)
    
    if respuesta in opciones:
        if isinstance(opciones[respuesta], dict):
            if respuesta == "0":
                if historial:
                    realizar_pregunta(historial.pop(), historial)
                else:
                    print("\nNo hay preguntas anteriores.\n")
                    realizar_pregunta(pregunta)
            else:
                historial.append(pregunta)
                realizar_pregunta(opciones[respuesta], historial)
        else:
            print(opciones[respuesta])
    elif respuesta == "0":
        if historial:
            realizar_pregunta(historial.pop(), historial)
        else:
            print("\nNo hay preguntas anteriores.\n")
            realizar_pregunta(pregunta)
    elif respuesta == "9":
        print("\nAdios! Vuelva pronto!\n")
        return
    else:
        print("\nOpción inválida. Por favor, selecciona una opción válida.\n")
        realizar_pregunta(pregunta, historial)

realizar_pregunta(preguntas[0])