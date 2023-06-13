import math

def calcular_hipotenusa():
    hipotenusa = math.sqrt((cat_a ** 2) + (cat_b ** 2))
    return hipotenusa

if __name__ == "__main__":
    cat_a = 4
    cat_b = 3
    print("La longitud de la hipotenusa es: ", calcular_hipotenusa())