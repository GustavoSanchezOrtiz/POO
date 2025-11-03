from tkinter import *
i = True
def cambiarTexto():
    global i 
    if i == True:
        mensajeCambiante.config(
            text="Soy el texto que cambio"
        )
        i = False
    elif i == False:
        mensajeCambiante.config(
        text="Texto Original"
    )
        i = True


def regresarTexto():
    mensajeCambiante.config(
        text="Texto Original"
    )


ventana= Tk()
ventana.title("uso de botones")
ventana.geometry("800x600")
ventana.state("zoomed")
frame_principal = Frame(ventana)
frame_principal.config(
    bg= "red",
    height= 50,
    width= 800,
    border=2,
    relief= GROOVE
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

label_titulos = Label(frame_principal, text= "uso de botones")
label_titulos.config(
    bg="red",
    width=20
)
label_titulos.pack(pady=10)

mensajeCambiante = Label(ventana, text="Texto Original")
mensajeCambiante.pack()

botonDeCambiar= Button(ventana, text="cambiar texto",command=cambiarTexto)
botonDeCambiar.pack()

botonDeRegreso= Button(ventana, text="Regresion a original",command=regresarTexto)
botonDeRegreso.pack()

ventana.mainloop()
