from Casilla import Casilla
from Lista import Lista
from Lista import ListaCircular
from Pregunta import Pregunta
from random import *

class Juego:
    def __init__ (self, num):
        self.leerArchivoPreguntas()
        self.leerArchivoPreguntasRuleta()
        self.leerTablero()
        self.num_jug = num
        self.jugadores = [0 for i in range(num)]

    def leerArchivoPreguntas (self):
        archivo = open("Preguntas.csv","r",encoding='utf-8')
        self.preguntas = Lista()

        linea = archivo.readline()
        while (linea != ""):
            datos = linea.split(";")
            pregunta = Pregunta(datos[0], datos[1:-1], datos[-1][:-1])
            self.preguntas.agregarNodo(pregunta)
            linea = archivo.readline()
        archivo.close()     

    def leerTablero (self):
        archivo = open("Tablero.csv","r",encoding='utf-8')
        self.tablero = Lista()

        linea = archivo.readline()
        while (linea != ""):
            datos = linea.split(";")
            casilla = Casilla(int(datos[0]), int(datos[1]), int(datos[2][:-1]), 0, 0)
            self.tablero.agregarNodo(casilla)
            linea = archivo.readline()
        archivo.close()

    def leerArchivoPreguntasRuleta (self):
        archivo = open("Preguntas-VoF.csv","r",encoding='utf-8')
        self.preguntas_ruleta = ListaCircular()

        linea = archivo.readline()
        while (linea != ""):
            datos = linea.split(";")
            pregunta = Pregunta(datos[0], datos[1:-1], datos[-1][:-1])
            self.preguntas_ruleta.agregarNodo(pregunta)
            linea = archivo.readline()
        archivo.close()       

    def bienvenida (self):
        print("Bienvenido a Data Run!!")

    def inicioJuego (self):
        print("Para empezar ingrese los nombres de los 2 jugadores")
        self.jug1 = input("Jugador 1:")
        self.jug2 = input("Jugador 2:")
        print("")
    
    def verificarGanador (self):
        for i in range(len(self.jugadores)):
            if self.jugadores[i] == 30:
                return i
        return -1

    def tirarDado (self):
        return randint(1, 6)

    def jugar (self):
        turno = 0
        while (self.verificarGanador() < 0):
            print("Turno del jugador ", turno)
            print("-> Tirando los dados")
            dado = self.tirarDado()
            print("\t-> Resultado del dado: ", dado)

            if (self.jugadores[turno] + dado > 30):
                print("\t-> Pierdes tu turno!! Tienes que llegar exactamente a la casilla 30 para ganar")
            else:
                self.jugadores[turno] += dado
                self.casillaCaida(self.jugadores[turno])

            turno += 1
            turno = turno % self.num_jug
            input("Presiona Enter para continuar...")

        self.definirGanador(self.verificarGanador())

    def definirGanador (self, ganador):
        print("Ha ganado el jugador ", ganador, "!!!")

    def casillaCaida(self, pos):
        casilla = self.tablero.obtenerNodo(pos)
        tipo_casilla = casilla.dato.tipo
        dato_casilla = casilla.dato.info
        print("\t-> Ha caido en la casilla ", pos)
        if (tipo_casilla == 0):
            print("\t\t-> Sin efectos")
        elif (tipo_casilla == 1):
            print("\t\t-> Pregunta Sorpresa")
            pregunta = self.preguntas.obtenerNodo(dato_casilla).dato
            self.hacerPregunta(pregunta)
        elif (tipo_casilla == 2):
            print("\t\t-> Juega la ruleta de Preguntas")
            self.jugarRuleta()
        elif (tipo_casilla == 3):
            print("\t\t-> Casilla Especial")
    
    def jugarRuleta (self):
        print("\t\t-> Girando la ruleta...")
        pregunta = self.preguntas_ruleta.obtenerNodo(randint(0, 50)).dato
        self.hacerPregunta(pregunta)
    
    def hacerPregunta (self, pregunta):
        print("\t\t| < La pregunta es: >")
        print("\t\t| ", pregunta.pregunta)
        for i in range(len(pregunta.respuestas)):
            print("\t\t| ",chr (i + 65), ". ", pregunta.respuestas[i])
        print("Ingrese su respuesta correcta...")
        respuesta = input("")

        if (respuesta == pregunta.respuesta_correcta):
            print("Correcto!!!")
            return True
        else:
            print("Erróneo, la respuesta correcta era ", pregunta.respuesta_correcta)
            return False