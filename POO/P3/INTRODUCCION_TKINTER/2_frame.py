from tkinter import *


ventana = Tk()
ventana.title("uso de frame")
alto_de_pantalla = ventana.winfo_screenheight()
ancho_de_pantalla = ventana.winfo_screenwidth()
ventana.geometry(f"{ancho_de_pantalla}x{alto_de_pantalla}")
ventana.state("zoomed")


marco = Frame(ventana,width=300, height=200, bg="silver", borderwidth=1, relief=SOLID)
marco.pack_propagate(False)
marco.pack(pady=100)

marco2 = Frame(marco, width=100, height=50, bg="blue", border=2, relief=GROOVE).pack(padx=50, pady=50)

ventana.mainloop()
