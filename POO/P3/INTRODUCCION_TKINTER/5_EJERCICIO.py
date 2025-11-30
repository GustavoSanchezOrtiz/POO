from tkinter import *

def cambiarTexto():
    mensaje_cambiante.config(
        text="Bienvenido"
    )

def regresarTexto():
    mensaje_cambiante.config(
        text="Nombre: \n Contraseña: "
    )

ventana=Tk()
ventana.title("Uso de Botones")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    bg="silver",
    width=800,
    height=50,
    border=2,
    relief=GROOVE
)
frame_principal.pack(pady=10)

label_titulo=Label(frame_principal, text="Uso de Botones")
label_titulo.config(
    bg="silver",
    width=20
)

frame_principal.pack_propagate(False)

label_titulo.pack(pady=10)

mensaje_cambiante=Label(ventana,text="Texto Original")
mensaje_cambiante.pack()

label_nombre=Label(ventana, text="Nombre: ")
label_nombre.config(
    bg="silver",
    width=20
)
label_nombre.pack(pady=10)

label_contraseña=Label(ventana, text="Contraseña: ")
label_contraseña.config(
    bg="silver",
    width=20
)
label_contraseña.pack(pady=10)


boton_cambiar=Button(ventana,text="Entrar",command=cambiarTexto)#Command es la accion a realizar
boton_cambiar.pack()

boton_regresar=Button(ventana,text="Salir",command=regresarTexto)
boton_regresar.pack()

#textos con nombre y contraseña y luego un boton de iniciar sesion, y cuando de click un mensjae que diga bienvenido inicio sesion en otra ventana

ventana.mainloop()