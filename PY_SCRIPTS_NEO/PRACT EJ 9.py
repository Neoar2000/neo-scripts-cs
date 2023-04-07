salario = int(input("Introduzca su salario mensual: "))
antiguedad = int(input("Introduzca sus años de antiguedad en la empresa: "))
if antiguedad < 1:
    utilidad = 0.05
elif antiguedad >= 1 and antiguedad < 2:
    utilidad = 0.07   
elif antiguedad >= 2 and antiguedad < 5:
    utilidad = 0.10
elif antiguedad >= 5 and antiguedad < 10:
    utilidad = 0.15
elif antiguedad >= 10:
    utilidad = 0.20

bono = salario * utilidad

print("Su bono es de: ", bono)