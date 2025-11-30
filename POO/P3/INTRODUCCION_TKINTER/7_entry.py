from tkinter import *

def haz_click():
    lbl_main.config(bg="green",
                fg="red",
                width=50,
                height=4,
                font=("Arial",30,"bold"),
                border=2,
                relief=GROOVE,
                text="POO con python"
                )
    
def regresar_click():
    lbl_main.config(bg="lightblue",
                fg="darkblue",
                width=50,
                height=4,
                font=("Helvetica",30,"italic"),
                border=2,
                relief=GROOVE
                )

    

ventana = Tk()
ventana.title("entry")
ventana.geometry("500x500")

lbl_main = Label(ventana, text="Acceso al sistema", bg="Blue")
lbl_main.config(bg="lightblue",
                fg="darkblue",
                width=50,
                height=4,
                font=("Helvetica",30,"italic"),
                border=2,
                relief=GROOVE
                )
lbl_main.pack(pady=50)

btn_entrada = Button(ventana,text="haz click aqui")
btn_entrada.config(
    fg="white",
    activeforeground="yellow",
    activebackground="black",
    width=15,
    font=("Comic sans",20,"bold"),
    command=haz_click
)
btn_entrada.pack()

btn_regresar = Button(ventana, text="Regresar click aqui",font=("Arial",20,"bold"), width=15,command=regresar_click)
btn_regresar.pack(pady=5)

lbl_nombre = Label(ventana, text="Ingrese el nombre: ")
lbl_nombre.pack(pady=5)

txt_nombre = Entry(ventana, width=10)
txt_nombre.pack()

lbl_password = Label(ventana, text="Ingrese la contraseña: ")
lbl_password.pack(pady=5)
txt_password = Entry(ventana, width=10, show="*")
txt_password.pack()

ventana.mainloop()