import tkinter as tk 

def mostrar_resultado_scale():
    lbl_valor_seleccionado.config(text=f"Valor seleccionado por el usuario: {var_scala1.get()}")

ventana = tk.Tk()

ventana.geometry("500x500")
ventana.title("scale")
ventana.state("zoomed")

btn_mostrar_valor = tk.Button(ventana, text="Mostrar valor", command=mostrar_resultado_scale)
btn_mostrar_valor.pack()

lbl_valor_seleccionado = tk.Label(ventana, text="")
lbl_valor_seleccionado.pack()

var_scala1 = tk.IntVar()
scl_scala1 = tk.Scale(ventana, from_=0, to=100, orient="horizontal", variable= var_scala1)
scl_scala1.pack()

ventana.mainloop()