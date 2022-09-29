import tkinter as tk
from tkinter import *
import tkinter as tk
from templates.welcome import welcome
from templates.MenuBar import  MenuBar
class Ventana(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("800x500")
        self.title("Juego de Preguntas")
        #self.img_welcome = tk.PhotoImage(file="Img/welcome.gif")
        self.config(bg="black")
        self.__create_widgets()

    def __create_widgets(self):
        frameinicio= welcome(self,"pagina de inicio")
        frameinicio.grid()
        # create the menu
        self.menubar = MenuBar(self,frameinicio)
        self.config(menu=self.menubar)
