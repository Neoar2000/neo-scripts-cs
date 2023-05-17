from Preguntas import pregunta

preg_prompt = [
"Cual es la capital de Bolivia?\n(a) La Paz\n(b) Sucre\n(c) Santa Cruz de la Sierra\n\n",
"Cual es la capital de Peru?\n(a) Lima\n(b) Cuzco\n(c) Arequipa\n\n",
"Cual es la capital de Colombia?\n(a) Bogota\n(b) Medellin\n(c) Cali\n\n",
]

preguntas = [
    pregunta(preg_prompt[0], "b"),
    pregunta(preg_prompt[1], "a"),
    pregunta(preg_prompt[2], "a")
]

def test(preguntas):
    puntaje = 0
    for pregunta in preguntas:
        answer = input(pregunta.prompt)
        if answer == pregunta.respuesta:
            puntaje += 1
    print("Respondiste", puntaje, "de", len(preg_prompt), "correctamente.")

test(preguntas)