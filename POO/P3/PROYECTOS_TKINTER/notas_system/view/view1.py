from tkinter import *
from controller.controlador1 import controlador
class Vista:
    def __init__(self,ventana:Tk):
        ventana.title("Gestión de notas")
        ventana.geometry("800x600")
        ventana.resizable(0,0)
        self.menu_principal(ventana)

    def menu_principal(self,ventana):
        self.limpiar_ventana(ventana)
        Label(ventana,text=".::Menú principal::.").pack()
        Button(ventana,text="1.-Registro",width=15,command=lambda:self.registro(ventana)).pack(pady=15)
        Button(ventana,text="2.-Login",width=15,command=lambda:self.login(ventana)).pack(pady=15)
        Button(ventana,text="3.-Salir",width=15,command=lambda:ventana.destroy()).pack(pady=15)

    def registro(self,ventana):
        self.limpiar_ventana(ventana)
        Label(ventana,text=".::Registro::.").pack(pady=5)
        Label(ventana,text="¿Cuál es tu nombre?").pack(pady=15)
        txt_nombre= Entry(ventana)
        txt_nombre.pack()
        txt_nombre.focus()
        Label(ventana,text="¿Cuales son tus apellidos?").pack(pady=15)
        txt_apellido = Entry(ventana)
        txt_apellido.pack()
        Label(ventana,text="Ingresa tu email").pack(pady=15)
        txt_email = Entry(ventana)
        txt_email.pack()
        Label(ventana,text="Ingresa tu contraseña").pack(pady=15)
        txt_contra = Entry(ventana,show="*")
        txt_contra.pack()
        Button(ventana,text="Registrar",width=15,command=lambda: self.accion_registrar(txt_nombre.get(), txt_apellido.get(), txt_email.get(), txt_contra.get(), ventana)).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:self.menu_principal(ventana)).pack(pady=15)

    def accion_registrar(self, txt_nombre, txt_apellido, txt_email, txt_contra, ventana):
        controlador.registro(txt_nombre, txt_apellido, txt_email, txt_contra)
        self.login(ventana)

    
    def login(self,ventana):
        self.limpiar_ventana(ventana)
        Label(ventana,text=".::Inicio de sesión::.").pack(pady=5)
        Label(ventana,text="Ingresa tu email").pack(pady=15)
        txt_email = Entry(ventana)
        txt_email.pack()
        txt_email.focus()
        Label(ventana,text="Ingresa tu contraseña").pack(pady=15)
        txt_contra = Entry(ventana,show="*")
        txt_contra.pack()
        Button(ventana,text="Entrar",width=15,command=lambda:self.accion_inicio_de_sesion(txt_email.get(), txt_contra.get(), ventana),).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:self.menu_principal(ventana)).pack(pady=15)

    def accion_inicio_de_sesion(self, txt_email, txt_contra, ventana):
        ID_usuario, Nombre_usuario, Apellido_usaurio = controlador.inicio_de_sesion(txt_email, txt_contra)
        self.ID_usuario = ID_usuario
        self.Nombre_usuario = Nombre_usuario
        self.Apellido_usuario = Apellido_usaurio
        self.menu_notas(ventana)

    def menu_notas(self,ventana):
        self.limpiar_ventana(ventana)
        Label(ventana,text=f".::Bienvenido {self.Nombre_usuario} {self.Apellido_usuario}, has iniciado sesión::.").pack()
        Button(ventana,text="1.-Crear",width=15,command=lambda:self.crear_nota(ventana)).pack(pady=15)
        Button(ventana,text="2.-Mostrar",width=15,command=lambda:self.mostrar_nota(ventana)).pack(pady=15)
        Button(ventana,text="3.-Cambiar",width=15,command=lambda:self.cambiar_nota(ventana)).pack(pady=15)
        Button(ventana,text="4.-Eliminar",width=15,command=lambda:self.eliminar_nota(ventana)).pack(pady=15)
        Button(ventana,text="5.-Regresar",width=15,command=lambda:self.menu_principal(ventana)).pack(pady=15)

    def crear_nota(self,ventana):
        self.limpiar_ventana(ventana)
        Label(ventana,text=".::Crear nota::.").pack()
        Label(ventana,text="Titulo").pack(pady=15)
        txt_titulo= Entry(ventana)
        txt_titulo.pack()
        txt_titulo.focus()
        Label(ventana,text="Descripción").pack(pady=15)
        txt_desc = Entry(ventana)
        txt_desc.pack()
        Button(ventana,text="Guardar",width=15,command=lambda:controlador.crear_nota(self.ID_usuario, titulo=txt_titulo.get(), descripcion=txt_desc.get())).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:self.menu_notas(ventana)).pack(pady=15)

    def mostrar_nota(self,ventana):
        self.limpiar_ventana(ventana)
        Label(ventana,text=f"{self.Nombre_usuario}, tus notas son").pack()
        filas = ""
        registros = controlador.conseguir_nota_de_usuario_especifico(self.ID_usuario)
        i = 1
        if registros and len(registros)>0:
            for fila in registros:
                filas += (
                f"Nota: {i}\n"
                f"ID {fila[0]} .- Título: {fila[2]}, Fecha de creación: {fila[4]}\n"
                f"Descripción: {fila[3]}\n\n"
                )
                i += 1
        else:
            filas = "No hay registros"
        Label(ventana,text=filas).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:self.menu_notas(ventana)).pack(pady=15)

    def cambiar_nota(self,ventana):
        self.limpiar_ventana(ventana)
        Label(ventana,text="Usuario, vamos a cambiar una nota").pack()
        Label(ventana,text="ID de la nota a cambiar").pack(pady=15)
        txt_id= Entry(ventana)
        txt_id.pack()
        txt_id.focus()
        Label(ventana,text="Nuevo Titulo").pack(pady=15)
        txt_titulo= Entry(ventana)
        txt_titulo.pack()
        Label(ventana,text="Nueva Descripción").pack(pady=15)
        txt_desc = Entry(ventana)
        txt_desc.pack()
        Button(ventana,text="Guardar",width=15,command=lambda: controlador.modificar_nota(id = txt_id.get(), titulo=txt_titulo.get(), descripcion=txt_desc.get())).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:self.menu_notas(ventana)).pack(pady=15)


    def eliminar_nota(self,ventana):
        self.limpiar_ventana(ventana)
        Label(ventana,text=f"{self.ID_usuario}, vamos a eliminar una nota").pack()
        Label(ventana,text="ID de la nota a eliminar").pack(pady=15)
        txt_id= Entry(ventana)
        txt_id.pack()
        txt_id.focus()
        Button(ventana,text="Eliminar",width=15,command=lambda: controlador.eliminar_nota(txt_id.get())).pack(pady=15)
        Button(ventana,text="Volver",width=15,command=lambda:self.menu_notas(ventana)).pack(pady=15)




    def limpiar_ventana(self,ventana):
        for widget in ventana.winfo_children():
            widget.pack_forget()