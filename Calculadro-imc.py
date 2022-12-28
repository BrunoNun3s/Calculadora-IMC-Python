from tkinter import *
from tkinter import ttk
import tkinter as tk

def IMC():
    P = Peso.get()
    A = Altura.get()
    IMC = float(Peso.get()) / float(Altura.get())**2
    Textimc = Label(window, text=f" seu IMC é: {IMC}")
    Textimc.place(x=105, y=190)

    TextStatus = Label(window, text="STATUS: ")
    TextStatus.place(x=105, y=215)
    if IMC < 18.5:
        TextStatus = Label(window, text="STATUS: ABAIXO DO PESO")
        TextStatus.place(x=105, y=215)
    elif IMC >= 18.5 and IMC < 25:
        TextStatus = Label(window, text="STATUS: NORMAL")
        TextStatus.place(x=105, y=215)
    elif IMC >= 25 and IMC < 30:
        TextStatus = Label(window, text="STATUS: SOBREPESO")
        TextStatus.place(x=105, y=215)
    elif IMC >=30 and IMC < 40:
        TextStatus = Label(window, text="STATUS: OBESIDADE")
        TextStatus.place(x=105, y=215)
    else:
        TextStatus = Label(window, text="STATUS: OBESIDADE MÓRBIDA")
        TextStatus.place(x=105, y=215)

window = Tk()

window.title('Calculadora-IMC')
window.geometry("300x250")
window.config(background="#6b70ff")

t1 = Label(window, text="Digite seu Peso:", background="#6b70ff")
t1.place(x=13, y=50)
Peso = Entry(window, width=30,)
Peso.place(x=100, y=50)

t2 = Label(window, text="Digite sua Altura:", background="#6b70ff")
t2.place(x=5, y=100)
Altura = Entry(window, width=30,)
Altura.place(x=100, y=100)

Button = Button(window, text="Calcular IMC", command=IMC)
Button.place(x=145, y=150)



mainloop()
