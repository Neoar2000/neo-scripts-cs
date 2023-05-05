import math

def calcular_trigonometricas(angulo_grados):
    angulo_radianes = math.radians(angulo_grados)

    seno = math.sin(angulo_radianes)
    coseno = math.cos(angulo_radianes)
    tangente = math.tan(angulo_radianes)
    cotangente = 1 / tangente
    secante = 1 / coseno
    cosecante = 1 / seno

    resultados = {
        "seno": seno,
        "coseno": coseno,
        "tangente": tangente,
        "cotangente": cotangente,
        "secante": secante,
        "cosecante": cosecante
    }

    return resultados

angulo_grados = float(input("Introduzca el ángulo en grados: "))

resultados = calcular_trigonometricas(angulo_grados)

for funcion, valor in resultados.items():
    print(f"{funcion.capitalize()}: {valor}")
