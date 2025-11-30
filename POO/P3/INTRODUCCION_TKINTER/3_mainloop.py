from tkinter import *

ventana = Tk()
ventana.title("mailoop")
ventana.geometry("800x600")
ventana.state("zoomed")

ventana=Tk()
ventana.title("Main-loop")
ventana.geometry("800x600")

marco=Frame(ventana)
marco.config(
    bg="#af06be40",
    bd=10,
    width=600,
    height=400,
    relief=RAISED
)
marco.pack(side=BOTTOM,anchor=SW)

mainloop()