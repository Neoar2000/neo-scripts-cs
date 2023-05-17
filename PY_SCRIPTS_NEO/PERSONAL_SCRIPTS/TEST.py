from Preguntas import pregunta

preg_prompt = [
"De que color es el cielo?\n(a) Azul\n(b) Negro\n(c) Rojo\n\n",
"Que lenguaje de programación estamos llevando en la Cato?\n(a) C++\n(b) Python\n(c) JavaScript\n\n",
"Quien creo la Mac?\n(a) Samsung\n(b) Microsoft\n(c) Apple\n\n",
]

preguntas = [
    pregunta(preg_prompt[0], "a"),
    pregunta(preg_prompt[1], "b"),
    pregunta(preg_prompt[2], "c")
]

def test(preguntas):
    puntaje = 0
    for pregunta in preguntas:
        answer = input(pregunta.prompt)
        if answer == pregunta.respuesta:
            puntaje += 1
    print("Respondiste", puntaje, "de", len(preg_prompt), "correctamente.")

test(preguntas)