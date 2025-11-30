import tkinter as tk 

def mostrar_seleccion():
    seleccion = var_seleccion.get()
    if seleccion == "Opcion1":
        lbl_resultado.config(text="Opcion1")
    elif seleccion == "Opcion2":
        lbl_resultado.config(text="Opcion2")
    elif seleccion == "Opcion3":
        lbl_resultado.config(text="Opcion3")
    else:
        lbl_resultado.config(text="Porfavor seleccione una casilla")

ventana = tk.Tk()

ventana.geometry("500x500")
ventana.title("radioButton")
ventana.state("zoomed")

var_seleccion = tk.StringVar()
radioButton_opcion1 = tk.Radiobutton(ventana,text="Opcion1", variable=var_seleccion,value="Opcion1")
radioButton_opcion1.pack()

radioButton_opcion1 = tk.Radiobutton(ventana,text="Opcion2", variable=var_seleccion,value="Opcion2")
radioButton_opcion1.pack()

radioButton_opcion1 = tk.Radiobutton(ventana,text="Opcion3", variable=var_seleccion,value="Opcion3")
radioButton_opcion1.pack()

btn_seleccion = tk.Button(ventana, text="Mostrar seleccion", command=mostrar_seleccion).pack()

lbl_resultado = tk.Label(ventana, text="")
lbl_resultado.pack()

ventana.mainloop()

