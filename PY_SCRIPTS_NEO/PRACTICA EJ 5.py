letra = str(input("Introduzca una letra: "))
if len(letra) == 1 and letra.isalpha():
    if letra in "aeiou":
        print("Vocal")
    else:
        print("Consonante")
else:
    print("Eso no es un caracter valido.")