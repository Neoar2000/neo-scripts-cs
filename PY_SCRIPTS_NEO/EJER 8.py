total = int(input("Ingrese el monto total de la compra: "))
descuento = 0
if total > 100:
    descuento = total * 0.05
    print("El precio con descuento es de:", total - descuento)
elif total < 100:
    print("El precio total es de:", total)
