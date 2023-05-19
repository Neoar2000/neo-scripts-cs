edad = int(input("Introduzca la edad de la persona: "))
if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 60:
    print("Adulto")
elif edad >= 60:
    print("Adulto mayor")