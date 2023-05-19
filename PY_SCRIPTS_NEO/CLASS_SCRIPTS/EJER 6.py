fecha1 = input("Ingrese la fecha en formato DD/MM/AAAA: ")
fecha2 = input("Ingrese otra fecha en formato DD/MM/AAAA: ")

dia1, mes1, ano1 = map(int, fecha1.split('/'))
dia2, mes2, ano2 = map(int, fecha2.split('/'))

if ano1 > ano2 or (ano1 == ano2 and mes1 > mes2) or (ano1 == ano2 and mes1 == mes2 and dia1 > dia2):
    dia1, mes1, ano1, dia2, mes2, ano2 = dia2, mes2, ano2, dia1, mes1, ano1

dias = (ano2 - ano1) * 360 + (mes2 - mes1) * 30 + (dia2 - dia1)
print("La diferencia entre las fechas es de", dias, "días.")