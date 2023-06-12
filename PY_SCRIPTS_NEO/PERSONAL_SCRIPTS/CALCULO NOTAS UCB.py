import os

os.system('cls' if os.name == 'nt' else 'clear')
print("Bienvenido al sistema de cálculo de notas de la UCB!\n")
parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("\nIngrese la nota del segundo parcial: "))

promedio = (parcial1 + parcial2) / 2

if promedio >= 60:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Su nota de habilitacion es:", promedio)
    final = float(input("\nIngrese la nota del examen final: "))
    if final >= 90:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("El estudiante ha APROBADO el curso con una nota final de:", final, "\n\nFelicitaciones por su excelencia académica en la UCB!")
    elif final >= 51:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("El estudiante ha APROBADO el curso con una nota final de:", final)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("El estudiante ha REPROBADO el curso con una nota final de:", final)
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("El estudiante ha REPROBADO el curso con una nota de habilitacion de:", promedio)