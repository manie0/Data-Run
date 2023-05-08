import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from PIL import Image, ImageTk

class VentanaJugadores (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.jug1 = "Jugador 1"
        self.jug2 = "Jugador 2"

        #Agregar Contenido de la ventana
        image1 = Image.open("images/Jugadores.png")
        portada = ImageTk.PhotoImage(image1)

        label = tk.Label(self, image=portada)
        label.image = portada
        label.place(x=0, y=0)

        self.emp = ImageTk.PhotoImage(Image.open("images/boton inicio.png"))
        boton = tk.Button(self, image=self.emp,
                            command=lambda: self.EmpezarJuego())
        boton.place(x=660, y=800)

        self.text1 = tk.StringVar()  
        self.text2 = tk.StringVar()  
        nameEntered = ttk.Entry(self, width = 80, textvariable = self.text1)
        nameEntered.place(x=180, y=200)
        nameEntered2 = ttk.Entry(self, width = 80, textvariable = self.text2)
        nameEntered2.place(x=1260, y=200)

    def EmpezarJuego (self):
        self.jug1 = self.text1.get()
        self.jug2 = self.text2.get()

        print("-----------------------------||-----------------------------")
        print("Registrado jugador 1 : ", self.jug1)
        print("Registrado jugador 2 : ",self.jug2)
        print("-----------------------------||-----------------------------")

        self.controller.mostrarVentana("VentanaJuego")

    def obtenerJugadores (self):
        return [self.jug1, self.jug2]
    
    def ejecutar (self):
        pass