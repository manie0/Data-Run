import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from PIL import Image, ImageTk

class VentanaGanador (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Agregar Contenido de la ventana
        img = Image.open("images/Portada.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.img = ImageTk.PhotoImage(img)
        self.my_label = tk.Canvas(self, width=self.img.width(), height=self.img.height())
        self.my_label.create_image(0, 0, image=self.img, anchor=tk.NW)
        self.canvas_text = self.my_label.create_text(800, 600, text = "Felicidades jugador, has ganado la partida!!!", fill="white", font=('Times 45 bold'), justify=tk.CENTER, width=1500)
        self.my_label.place(x=0, y=0)

        img = Image.open("images/regresar.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.reg = ImageTk.PhotoImage(img)
        boton = tk.Button(self, image=self.reg,
                            command=lambda: controller.mostrarVentana("VentanaInicio"))
        boton.place(x=0, y=0)


    def ejecutar (self):
        self.my_label.itemconfig(self.canvas_text, text=f"Felicidades {self.controller.obtenerGanador()}, has ganado la partida!!!", justify=tk.CENTER)