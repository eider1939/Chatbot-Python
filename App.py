from tkinter import *
import tkinter as tk
from tkinter import ttk
from background import chat
from functools import partial
####
# funcion enviar

def enviar(mensaje):
    texto=mensaje.get()
    respuesta=chat.get_response(texto)
    mostrar(texto,respuesta)

def mostrar(texto,respuesta):
    text.config(state="normal")
    text.insert(END,"You: "+texto+"\n")
    text.insert(END,"Bot: "+respuesta+"\n")
    text.config(state=DISABLED)

root=Tk()
root.title("Chatbot Python")
root.geometry("400x380")

label = Label(root, text ='Welcome al chatbot', font = "60")
label.grid(row=0, column=2,padx=10,pady=10,columnspan=2)

text=Text(root,height=10,width=39,font=15)
text.grid(row=2,column=2,padx=10,pady=10,sticky="ew",columnspan=2)
text.config(state=DISABLED)

sb=Scrollbar(root,orient=VERTICAL)
sb.grid(row=2,column=4,sticky=NS)
text.config(yscrollcommand=sb.set)
sb.config(command=text.yview)

label = Label(root, text ='Mensaje: ', font = "60")
label.grid(row=3, column=2,sticky="e")

mensaje=StringVar()
text_1=Entry(root,textvariable=mensaje)
text_1.grid(row=3,column=3,ipadx=50,ipady=3,padx=10,pady=10,sticky="w")

enviar = partial(enviar, mensaje)

button = Button(root, text="ENVIAR", font="60",command=enviar)
button.grid(row=4, column=2,columnspan=2,pady=12)

label = Label(root, text ='Autor: Alejandro Peña', font = "20")
label.grid(row=5, column=2,columnspan=2,sticky="e")
frame=Frame(
    root,bg="grey"
)
root.mainloop()