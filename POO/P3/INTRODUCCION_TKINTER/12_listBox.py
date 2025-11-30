import tkinter as tk 
import customtkinter as ctk

def mostrar_valor_seleccionado():
    try:
        valor = lst_lista1.get(lst_lista1.curselection())
        lbl_seleccion_del_usuario.config(text=f"La seleccion del usuario es: {valor}")
    except:
        lbl_seleccion_del_usuario.config(text=f"Porfavor seleccione un valor")
ventana = tk.Tk()

def cerrar_ventana():
    ventana.destroy()

opciones = ["Azul", "Rojo", "Negro", "Amarillo"]
lst_lista1 = tk.Listbox(ventana, width=50, height=4, selectmode="single")
lst_lista1.pack()
for i in opciones:
    lst_lista1.insert(tk.END, i)

ventana.geometry("500x500")
ventana.title("listBox")
ventana.state("zoomed")

btn_seleccion_del_usuario = ctk.CTkButton(ventana, text="Mostrar seleccion del usuario", corner_radius=20, command= mostrar_valor_seleccionado)
btn_seleccion_del_usuario.pack(pady = 5)

lbl_seleccion_del_usuario = tk.Label(ventana, text="")
lbl_seleccion_del_usuario.pack()

btn_cerrar = ctk.CTkButton (ventana, text="Salir", command= cerrar_ventana)
btn_cerrar.pack()

ventana.mainloop()