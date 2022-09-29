import tkinter as tk
from tkinter import *


class welcome(tk.Frame):
    def __init__(self, container,labeltext):
        super().__init__(container)
        frame_welcome=tk.Frame(self, background="black",width=700,height=500)
        frame_welcome.grid(sticky='news')
        photo1 = tk.Label(frame_welcome)
        photo1.grid(row=0, column=0,columnspan=2,sticky='news')
        tk.Label(frame_welcome, text="Aplicaion creada por: \nEider Alejandro Peña Dagua",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=2,column=1)



