from Juego import *
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from Aplicacion import Aplicacion

def empezar ():
    juego = Juego(2)
    juego.bienvenida()
    juego.jugar()

app = Aplicacion()
app.mainloop()