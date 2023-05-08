import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from Juego import Juego
from PIL import Image, ImageTk
import time


class VentanaJuego (tk.Frame):
    def __init__(self, parent, controller, jugadores):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.jugadores = jugadores
        self.juego = Juego(2)

        #Agregar Contenido de la ventana
        img = Image.open("images/Juego.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)

        self.fondo = ImageTk.PhotoImage(img)
        self.canva = tk.Canvas(self, width=self.fondo.width(), height=self.fondo.height())
        self.canva.create_image(0, 0, image=self.fondo, anchor=tk.NW)
        self.canva.place(x=0, y=0)

        img = Image.open("images/dado (6).png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        portada = ImageTk.PhotoImage(img)

        self.dado_img = tk.Label(self, image=portada)
        self.dado_img.image = portada
        pos = (int(1560*controller.width/1920), int(190*controller.height/1080))
        self.dado_img.place(x=pos[0], y=pos[1])

        img = Image.open("images/regresar.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.reg = ImageTk.PhotoImage(img)
        boton = tk.Button(self, image=self.reg,
                            command=lambda: controller.mostrarVentana("VentanaInicio"))
        boton.place(x=0, y=0)

        #Agregar Contenido de la ventana
        img = Image.open("images/tirar dados.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.boton_dados = ImageTk.PhotoImage(img)
        boton = tk.Button(self, image=self.boton_dados, compound = tk.BOTTOM,
                            command=lambda: self.jugarDados())
        pos = (int(1440*controller.width/1920), int(680*controller.height/1080))
        boton.place(x=pos[0], y=pos[1])

        #Mostrar fichas de jugadores

        self.jug1_x = int(self.juego.tablero.obtenerNodo(self.juego.jugadores[0]).dato.x*self.controller.width/1920)
        self.jug1_y = int(self.juego.tablero.obtenerNodo(self.juego.jugadores[0]).dato.y*self.controller.height/1080)

        img = Image.open("images/Jugador1.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.img1 = ImageTk.PhotoImage(img)
        self.canva.create_image(self.jug1_x, self.jug1_y, image=self.img1, anchor=tk.NW)

        self.jug2_x = int(self.juego.tablero.obtenerNodo(self.juego.jugadores[1]).dato.x*controller.width/1920)
        self.jug2_y = int(self.juego.tablero.obtenerNodo(self.juego.jugadores[1]).dato.y*controller.height/1080)
        
        img = Image.open("images/Jugador2.png")
        tam = (int(img.width*controller.width/1920), int(img.height*controller.height/1080))
        img = img.resize(tam)
        self.img2 = ImageTk.PhotoImage(img)
        self.canva.create_image(self.jug2_x, self.jug2_y, image=self.img2, anchor=tk.NW)

        self.tipo_pregunta = ""
        self.dado = 0

    def moverFicha (self):
        prev_x = self.jug1_x
        prev_y = self.jug1_y

        self.jug1_x = int(self.juego.tablero.obtenerNodo(self.juego.jugadores[0]).dato.x*self.controller.width/1920)
        self.jug1_y = int(self.juego.tablero.obtenerNodo(self.juego.jugadores[0]).dato.y*self.controller.height/1080)

        if (prev_x != self.jug1_x or prev_y != self.jug1_y):
            tiempo = time.time()
            fin = tiempo + 3
            inicio = tiempo
            dif = fin-inicio
            dif_x = self.jug1_x - prev_x
            dif_y = self.jug1_y - prev_y
            while (tiempo < fin):
                self.canva.create_image(0, 0, image=self.fondo, anchor=tk.NW)
                self.canva.create_image(self.jug2_x, self.jug2_y, image=self.img2, anchor=tk.NW)

                x = prev_x + int(dif_x * (tiempo - inicio)/dif)
                y = prev_y + int(dif_y * (tiempo - inicio)/dif)
                self.canva.create_image(x, y, image=self.img1, anchor=tk.NW)
                self.update()
                tiempo = time.time()
        self.canva.create_image(0, 0, image=self.fondo, anchor=tk.NW)
        self.canva.create_image(self.jug2_x, self.jug2_y, image=self.img2, anchor=tk.NW)
        self.canva.create_image(self.jug1_x, self.jug1_y, image=self.img1, anchor=tk.NW)
        self.update()

        prev_x = self.jug2_x
        prev_y = self.jug2_y

        self.jug2_x = int(self.juego.tablero.obtenerNodo(self.juego.jugadores[1]).dato.x*self.controller.width/1920)
        self.jug2_y = int(self.juego.tablero.obtenerNodo(self.juego.jugadores[1]).dato.y*self.controller.height/1080)

        if (prev_x != self.jug2_x or prev_y != self.jug2_y):
            tiempo = time.time()
            fin = tiempo + 3
            inicio = tiempo
            dif = fin-inicio
            dif_x = self.jug2_x - prev_x
            dif_y = self.jug2_y - prev_y
            while (tiempo < fin):
                self.canva.create_image(0, 0, image=self.fondo, anchor=tk.NW)
                self.canva.create_image(self.jug1_x, self.jug1_y, image=self.img1, anchor=tk.NW)

                x = prev_x + int(dif_x * (tiempo - inicio)/dif)
                y = prev_y + int(dif_y * (tiempo - inicio)/dif)
                self.canva.create_image(x, y, image=self.img2, anchor=tk.NW)
                self.update()
                tiempo = time.time()
        self.canva.create_image(0, 0, image=self.fondo, anchor=tk.NW)
        self.canva.create_image(self.jug1_x, self.jug1_y, image=self.img1, anchor=tk.NW)
        self.canva.create_image(self.jug2_x, self.jug2_y, image=self.img2, anchor=tk.NW)
        self.update()


    def jugarDados (self):
        turno = self.juego.turno
        print("Turno del jugador ", turno)      

        print("-> Tirando los dados")
        
        #Ejecutar animación de dados
        tiempo = time.time()
        fin = tiempo + 3
        inicio = tiempo
        dif = fin - inicio
        cont = 0
        
        while (tiempo < fin):
            if (((tiempo - inicio)/dif)*100 > cont):
                self.dado = self.juego.tirarDado()
                img = Image.open(f"images/dado ({self.dado}).png")
                tam = (int(img.width*self.controller.width/1920), int(img.height*self.controller.height/1080))
                img = img.resize(tam)
                imagen = ImageTk.PhotoImage(img)
                self.dado_img.configure(image=imagen)
                self.dado_img.image = imagen
                self.update()
                cont += 1
            tiempo = time.time()


        print("\t-> Resultado del dado: ", self.dado)


        #Mostrar dados

        #Ejecutar movimiento
        if (self.juego.jugadores[turno] + self.dado > 62):
            print("\t-> Pierdes tu turno!! Tienes que llegar exactamente a la casilla 30 para ganar")
            self.juego.aumentarTurno()
        else:
            self.casillaCaida(self.juego.jugadores[turno] + self.dado)

        #Definir ganador
        if (self.juego.verificarGanador() > 0):
            ganador = self.juego.definirGanador(self.juego.verificarGanador())
            self.controller.mostrarVentana("VentanaGanador")

    def casillaCaida(self, pos):
        casilla = self.juego.tablero.obtenerNodo(pos)
        tipo_casilla = casilla.dato.tipo
        dato_casilla = casilla.dato.info
        print("\t-> Ha caido en la casilla ", pos)
        if (tipo_casilla == 0):
            print("\t\t-> Sin efectos")
            self.juego.jugadores[self.juego.turno] += self.dado
            self.juego.aumentarTurno()
            self.moverFicha()
        elif (tipo_casilla == 1):
            print("\t\t-> Pregunta Sorpresa")
            pregunta = self.juego.preguntas.obtenerNodo(dato_casilla).dato
            self.tipo_pregunta = "VentanaPreguntaABCD"
            self.juego.jugadores[self.juego.turno] += self.dado
            self.moverFicha()
            self.controller.hacerPregunta("VentanaPreguntaABCD", pregunta)
        elif (tipo_casilla == 2):
            print("\t\t-> Juega la ruleta de Preguntas")
            self.tipo_pregunta = "VentanaPreguntaVF"
            self.juego.jugadores[self.juego.turno] += self.dado
            self.moverFicha()
            self.controller.mostrarVentana("VentanaRuleta")
        elif (tipo_casilla == 3):
            print("\t\t-> Casilla Especial")
            self.juego.jugadores[self.juego.turno] = dato_casilla
            self.juego.aumentarTurno()
            self.moverFicha()

    def ejecutar (self):
        print(self.juego.turno, "   ", self.juego.jugadores[self.juego.turno])

        if (self.controller.preguntaCorrecta(self.tipo_pregunta)[0] and self.controller.preguntaCorrecta(self.tipo_pregunta)[1]):
            self.juego.aumentarTurno()
        else:
            self.juego.jugadores[self.juego.turno] -= self.dado
            self.juego.aumentarTurno()
            self.moverFicha()