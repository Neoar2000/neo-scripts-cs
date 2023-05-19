def ultimapalabra():
    ultima_palabra = texto.split()[-1]
    return ultima_palabra

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    print("La ultima palabra del texto introducido es:", ultimapalabra())