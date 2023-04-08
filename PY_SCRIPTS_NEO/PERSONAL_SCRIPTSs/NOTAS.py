#Esta es una funcion que calcula notas finales.
def calcnote():
    nota1 = float(input("Introduzca su nota del primer parcial: "))
    nota2 = float(input("Introduzca su nota del segundo parcial: "))
    nota3 = float(input("Introduzca su nota del examen final: "))
    notafinal = (nota1 + nota2 + nota3) / 3
    if notafinal >= 51:
        print("Su nota final es: " + str(notafinal) + ". Usted ha APROBADO la carrera!")
    else:
        print("Su nota final es: " + str(notafinal) + ". Usted ha REPROBADO la carrera...")

calcnote()