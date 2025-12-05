
from tkinter import *
from view import view1

class App:
    def __init__(self,ventana):
        vista=view1.View(ventana)
    
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
    
