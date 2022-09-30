from tkinter import *
from background import chat
import tkinter as tk
#
#Funcion que llama a la parte logica del chatbot
def callback():
    text = Usuario_text.get(0.1,END)
    respuesta=chat.get_response(text)
    bot_text.insert(END,respuesta+"\n")

#root window
root = Tk()
#label
label = Label(root, text ='Welcome al chatbot', font = "60")
label.grid(row=0, column=2,columnspan=4,padx=10,pady=10)
#box text you
Usuario_text = Text(root, width=43, height=10, font=(("Times"), 10,"bold"), wrap=WORD, fg="white", bg="black")
Usuario_text.grid(row=1, column=1,rowspan=3, columnspan=3, padx=20)
Usuario_text.insert(END,"You: ")
#trext box bot
bot_text= Text(root, width=43, height=10, font=(("Times"), 10,"bold"), wrap=WORD, fg="white", bg="black")
bot_text.grid(row=1, column=4,rowspan=3,columnspan=3)
#incial text
bot_text.insert(END,"Bot: ")
#button enviar
button1 = Button(root, text="ENVIAR", font="60", command = callback )
button1.grid(row=5, column=3,columnspan=2,pady=12)

root.title("Chatbot Python")
root.geometry("675x300")
root.mainloop()