import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

from VentanaGanador import VentanaGanador
from VentanaInicio import VentanaInicio
from VentanaJuego import VentanaJuego
from VentanaJugadores import VentanaJugadores
from VentanaPreguntaABCD import VentanaPreguntaABCD
from VentanaPreguntaVF import VentanaPreguntaVF
from VentanaRuleta import VentanaRuleta
from Lista import Lista
from Juego import Juego

class Aplicacion (tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Crear contenedor
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.attributes('-fullscreen',True)
        
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        #Crear todas las ventanas
        self.frames = Lista()
        nombre = "VentanaInicio"
        frame = VentanaInicio(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames.agregarNodo([frame, nombre])
        nombre = "VentanaJugadores"
        frame = VentanaJugadores(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames.agregarNodo([frame, nombre])
        nombre = "VentanaJuego"
        frame = VentanaJuego(parent=container, controller=self, jugadores=[])
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames.agregarNodo([frame, nombre])
        nombre = "VentanaRuleta"
        frame = VentanaRuleta(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames.agregarNodo([frame, nombre])
        nombre = "VentanaPreguntaABCD"
        frame = VentanaPreguntaABCD(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames.agregarNodo([frame, nombre])
        nombre = "VentanaPreguntaVF"
        frame = VentanaPreguntaVF(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames.agregarNodo([frame, nombre])
        nombre = "VentanaGanador"
        frame = VentanaGanador(parent=container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames.agregarNodo([frame, nombre])

        self.mostrarVentana("VentanaInicio")

    def mostrarVentana(self, ventana):
        #Buscar Ventana en Lista
        nodo = self.frames.raiz
        while (nodo != None and nodo.dato[1] != ventana):
            nodo = nodo.next
    
        if (nodo != None):
            nodo.dato[0].tkraise()
            nodo.dato[0].ejecutar()
            return nodo.dato[0]

    def hacerPregunta (self, ventana, pregunta):
        vent= self.mostrarVentana(ventana)
        vent.cargarPregunta(pregunta)

    def preguntaCorrecta (self, ventana):
        #Buscar Ventana en Lista
        nodo = self.frames.raiz
        while (nodo != None and nodo.dato[1] != ventana):
            nodo = nodo.next
    
        if (nodo != None):
            return [nodo.dato[0].respondido, nodo.dato[0].respuesta_correcta]
        return [False, False]
    
    def obtenerGanador (self):
        #Buscar Ventana en Lista
        nodo = self.frames.raiz
        while (nodo != None and nodo.dato[1] != "VentanaJuego"):
            nodo = nodo.next
    
        if (nodo != None):
            return f"Jugador {nodo.dato[0].juego.verificarGanador()}"
        return "Jugador"