import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox

mensajeAplicacion='''La aplicación es un demo jugable que rememora a los clásicos juegos de rol de texto, para ello implementaremos los conceptos de la programación orientada a objetos vistos en clase. Se desarrollará la narración en un clásico ecosistema de fantasía medieval, inspirado en el juego Calabozos & Dragones.'''
def Aplicacion():
    messagebox.showinfo(title='Aplicación',
    message='Informacion Basica',
    detail=mensajeAplicacion)

def ayuda():
    messagebox.showinfo(title='Ayuda',
    message='Autores',
    detail='''Brayan David Caballero Fernández\nJohn Mauricio Mesa Echeverri\nEider Alejandro Peña Dagua\nSantiago Rivera Mejía''')


class MenuBar(tk.Menu):
    def __init__(self, container,frameinicio):
        
        super().__init__(container)
        # setup the grid layout manager
        self.frameinicio=frameinicio
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.__create_widgets()

    def __create_widgets(self):
        tk.Menu.__init__(self)
        menuArchivo = tk.Menu(self, tearoff=False)
        self.add_cascade(menu=menuArchivo,label='Archivo')
        menuArchivo.add_command(label="Aplicación", command=Aplicacion)
        menuArchivo.add_command(label="Salir")#, command=self.regresarInicio(self))
        menuProcesos= tk.Menu(self, tearoff=False)
        self.add_cascade(menu=menuProcesos, label='Procesos y Consultas')
        menuProcesos.add_command(label="Inventario")
        menuProcesos.add_separator()
        menuProcesos.add_separator()
        menuayuda = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Ayuda",menu=menuayuda)
        menuayuda.add_command(label="Ayuda", command=ayuda)
        menuLogin= tk.Menu(self, tearoff=False)
        self.add_cascade(label="Login",menu=menuLogin)
        menuLogin.add_command(label="Registarse")
        menuLogin.add_command(label="Ingresar")

