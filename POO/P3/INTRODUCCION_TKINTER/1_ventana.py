'''
   tkinter trabaja a traves de interfaces, es una biblioteca grafica que permite crear ventanas y elementos visuales en python
'''
from tkinter import *
import tkinter as tkin

ventana = tkin.Tk() 
ventana.title("Mi primer ventana")
ventana.geometry("800x600")
ventana.resizable(False,True)
ventana.mainloop() #metodo que permite tener la ventana abierta e interactuar