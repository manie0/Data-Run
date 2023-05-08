import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from PIL import Image, ImageTk
import random
from Juego import Juego
import time

class VentanaRuleta (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Agregar Contenido de la ventana
        img = Image.open("images/Ruleta.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        portada = ImageTk.PhotoImage(img)

        label = tk.Label(self, image=portada)
        label.image = portada
        label.place(x=0, y=0)

        img = Image.open("images/RuletaGiratoria.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        portada = ImageTk.PhotoImage(img)

        self.ruleta = tk.Label(self, image=portada)
        self.ruleta.image = portada
        pos = (int(660*controller.width/1920), int(100*controller.height/1080))
        self.ruleta.place(x=pos[0], y=pos[1])


        juego = Juego(2)
        self.preguntas_ruleta = juego.preguntas_ruleta

        img = Image.open("images/regresar.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.reg = ImageTk.PhotoImage(img)
        boton = tk.Button(self, image=self.reg,
                            command=lambda: controller.mostrarVentana("VentanaJuego"))
        boton.place(x=0, y=0)

        img = Image.open("images/Girar ruleta.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.boton_ruleta = ImageTk.PhotoImage(img)
        boton = tk.Button(self, image=self.boton_ruleta, compound = tk.BOTTOM,
                            command=lambda: self.girarRuleta())
        pos = (int(660*controller.width/1920), int(840*controller.height/1080))
        boton.place(x=pos[0], y=pos[1])

    def girarRuleta (self):
        pregunta = self.preguntas_ruleta.obtenerNodo(random.randint(0, 50)).dato
        print(pregunta.pregunta)

        tiempo = time.time()
        fin = tiempo + 3

        img = Image.open("images/RuletaGiratoria.png")
        tam = (int(img.width*self.controller.width/1920), int(img.height*self.controller.height/1080))
        img = img.resize(tam)
        rotacion = 0

        while (tiempo < fin):
            imagen = ImageTk.PhotoImage(img.rotate(rotacion))
            self.ruleta.configure(image=imagen)
            self.ruleta.image = imagen
            self.update()

            tiempo = time.time()
            rotacion += 10
            rotacion = rotacion%360

        tiempo = time.time()
        fin = tiempo + 3
        cambio = 0
        dif = fin - tiempo
        while (tiempo < fin):
            imagen = ImageTk.PhotoImage(img.rotate(rotacion))
            self.ruleta.configure(image=imagen)
            self.ruleta.image = imagen
            self.update()

            tiempo = time.time()
            rotacion += (10 - cambio)
            rotacion = rotacion%360

            if (fin != tiempo):
                cambio = int(dif/(fin-tiempo))
                if (cambio > 10):
                    cambio = 10

        tiempo = time.time()
        fin = tiempo + 3


        while (tiempo < fin):
            tiempo = time.time()

        self.controller.hacerPregunta("VentanaPreguntaVF", pregunta)

    def ejecutar (self):
        pass