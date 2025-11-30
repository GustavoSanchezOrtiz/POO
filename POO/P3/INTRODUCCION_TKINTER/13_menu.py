import tkinter as tk 
import customtkinter as ctk

def mensaje(tipo):
    resultado.config(text=f"{tipo}")

ventana = tk.Tk()

ventana.geometry("500x500")
ventana.title("menu")
ventana.state("zoomed")

menuBar = tk.Menu(ventana)
ventana.config(menu=menuBar)
archivoMenu = tk.Menu(menuBar , tearoff=1)
menuBar.add_cascade(label="Archivo" , menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda: mensaje("Nuevo Archivo") )
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar Archivo",command=lambda: mensaje("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar Archivo",command=ventana.quit)

edicionMenu = tk.Menu(menuBar , tearoff=1)
menuBar.add_cascade(label="Edicion" , menu=edicionMenu)
edicionMenu.add_command(label="Copiar",command=lambda: mensaje("Nueva copia") )
edicionMenu.add_command(label="Recortar",command=lambda: mensaje("Nuevo recorte") )
edicionMenu.add_separator()
edicionMenu.add_command(label="Cerrar Archivo",command=ventana.destroy) 

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()