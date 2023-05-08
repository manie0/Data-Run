import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from PIL import Image, ImageTk

class VentanaPreguntaVF (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Agregar Contenido de la ventana
        img = Image.open("images/PreguntaVF.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        portada = ImageTk.PhotoImage(img)

        label = tk.Label(self, image=portada)
        label.image = portada
        label.place(x=0, y=0)

        img = Image.open("images/regresar.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.reg = ImageTk.PhotoImage(img)
        boton = tk.Button(self, image=self.reg,
                            command=lambda: controller.mostrarVentana("VentanaJuego"))
        boton.place(x=0, y=0)

        img = Image.open("images/opcion V.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.img_botonV = ImageTk.PhotoImage(img)
        boton1 = tk.Button(self, image=self.img_botonV, compound = tk.BOTTOM,
                            command=lambda: self.seleccionarRespuesta("A"))
        pos = (int(480*controller.width/1920), int(660*controller.height/1080))
        boton1.place(x=pos[0], y=pos[1])

        img = Image.open("images/opcion F.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.img_botonF = ImageTk.PhotoImage(img)
        boton2 = tk.Button(self, image=self.img_botonF, compound = tk.BOTTOM,
                            command=lambda: self.seleccionarRespuesta("B"))
        pos = (int(1020*controller.width/1920), int(660*controller.height/1080))
        boton2.place(x=pos[0], y=pos[1])


        img = Image.open("images/tablero_texto.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.img = ImageTk.PhotoImage(img)
        self.my_label = tk.Canvas(self, width=self.img.width(), height=self.img.height())
        self.my_label.create_image(0, 0, image=self.img, anchor=tk.NW)
        tam_txt = int(25*controller.width/1920)
        pos = (int(800*controller.width/1920), int(100*controller.height/1080), int(1200*controller.width/1920))
        self.canvas_text = self.my_label.create_text(pos[0], pos[1], text = "Pregunta VF", fill="black", font=(f'Helvetica {tam_txt} bold'), justify=tk.CENTER, width=pos[2])
        pos = (int(180*controller.width/1920), int(100*controller.height/1080))
        self.my_label.place(x=pos[0], y=pos[1])

        self.respondido = False
        self.respuesta_correcta = False


    def cargarPregunta (self, pregunta):
        self.pregunta = pregunta
        texto = f"{pregunta.pregunta}"
        self.my_label.itemconfig(self.canvas_text, text=texto, justify=tk.CENTER)
        self.respondido = False
        self.respuesta_correcta = False

    def seleccionarRespuesta (self, respuesta):
        if (not self.respondido):
            if (self.pregunta.respuesta_correcta == respuesta):
                self.my_label.itemconfig(self.canvas_text, text="Respuesta correcta!!!\nPresiona el botón de regresar para seguir jugando", justify=tk.CENTER)
                self.respuesta_correcta = True
            else:
                self.my_label.itemconfig(self.canvas_text, text="Respuesta incorrecta!!!\nPierdes tu turno\nPresiona el botón de regresar para seguir jugando", justify=tk.CENTER)
                self.respuesta_correcta = False
            
            self.respondido = True

    def ejecutar (self):
        pass