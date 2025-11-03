from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
ventana.title("etiquetas")
ventana.state("zoomed")
etiqueta1 = Label(ventana, text="Nombre de la persona", bg="#FCC19D")
etiqueta1.pack_propagate(False)
etiqueta1.pack()

marco1= Frame(ventana, bg="silver", width=100, height=50)
marco1.pack_propagate(False)
marco1.pack()
etiqueta2 = Label(marco1, text="Soy una etiqueta!!!, en un marco!!").pack()

ventana.mainloop()
