fecha1 = input("Ingrese la fecha en formato DD/MM/AAAA: ")
fecha2 = input("Ingrese otra fecha en formato DD/MM/AAAA: ")

dia1, mes1, anio1 = map(int, fecha1.split('/'))
dia2, mes2, anio2 = map(int, fecha2.split('/'))

if anio1 > anio2 or (anio1 == anio2 and mes1 > mes2) or (anio1 == anio2 and mes1 == mes2 and dia1 > dia2):
    dia1, mes1, anio1, dia2, mes2, anio2 = dia2, mes2, anio2, dia1, mes1, anio1

dias = (anio2 - anio1) * 360 + (mes2 - mes1) * 30 + (dia2 - dia1)
print("La diferencia entre las fechas es de", dias, "días.")