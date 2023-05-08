import tkinter as tk
from PIL import Image, ImageTk

class VentanaInicio (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Agregar Contenido de la ventana
        #label = tk.Label(self, text="This is the start page")
        #label.pack(side="top", fill="x", pady=10)

        img = Image.open("images/Portada.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        portada = ImageTk.PhotoImage(img)

        label = tk.Label(self, image=portada)
        label.image = portada
        label.place(x=0, y=0)
        #label.pack()

        img = Image.open("images/boton inicio.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.emp = ImageTk.PhotoImage(image=img)
        boton = tk.Button(self, image=self.emp, width=self.emp.width(), height=self.emp.height(),
                            command=lambda: self.controller.mostrarVentana("VentanaJuego"))
        pos = (int(660*controller.width/1920), int(800*controller.height/1080))
        boton.place(x=pos[0], y=pos[1])
    
    def ejecutar (self):
        pass
