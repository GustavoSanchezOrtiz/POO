from tkinter  import *

def mostrar_estado():
    if opcion_res.get() == 1:
        lbl_resultado.config(text="Notificaciones activadas")
    else:
        lbl_resultado.config(text="Notificaciones desactivadas")

ventana = Tk()
ventana.geometry("500x500")
ventana.title("checkButton")

opcion_res = IntVar()
checkBox_notificaciones = Checkbutton(ventana, text="¿Deseas recibir notificaciones?", variable=opcion_res,onvalue=1,offvalue= 0)
checkBox_notificaciones.pack()

btn_confirmar = Button(ventana, text="Confirmar", command=mostrar_estado).pack()

lbl_resultado = Label(ventana, text="")
lbl_resultado.pack()


ventana.mainloop()