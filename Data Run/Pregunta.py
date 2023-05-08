class Pregunta:
    def __init__ (self, pregunta, respuestas, respuesta_correcta):
        self.pregunta = pregunta
        self.respuestas = respuestas
        self.respuesta_correcta = respuesta_correcta

    def __repr__(self) -> str:
        return self.pregunta