from tkinter import messagebox
from model.usuario import Usuario
from model.nota import Nota

class controlador():
    @staticmethod
    def registro(nombre, apellidos, email, password):
        resultado = Usuario.registrar(nombre, apellidos, email, password)
        if resultado:
            messagebox.showinfo(icon="info", message=f"{nombre} {apellidos}, se registro correctamente, con el email: {email}", title="Usuarios | Registro exitoso")
        else:
            messagebox.showerror(icon="error", message="Ocurrio un error porfavor intentelo de nuevo",title="Usuarios | Error" )

    @staticmethod
    def inicio_de_sesion(email, password):
        registro = Usuario.iniciar_sesion(email, password)
        if registro:
            messagebox.showinfo(icon="info", message=f"{registro[1]}, {registro[2]} iniciaste sesion correctamente", title="Usuarios | registro")
            return registro[0], registro[1], registro[2]
        else:
            messagebox.showerror(icon="error", message="Ocurrio un error porfavor intentelo de nuevo",title="Usuarios | Error" )

    @staticmethod
    def mensajes_de_confirmacion(confirmacion):
        if confirmacion:
            messagebox.showinfo(icon="info", message=f"Accion Realizada con exito", title="Notas")
        else:
            messagebox.showerror(icon="error", message="Ocurrio un error porfavor intentelo de nuevo",title="Notas | Error" )

    @staticmethod
    def crear_nota(ID_usuario, titulo, descripcion):
        confirmacion = Nota.crear(ID_usuario, titulo, descripcion)
        controlador.mensajes_de_confirmacion(confirmacion)
    
    @staticmethod
    def conseguir_nota_de_usuario_especifico(ID_usario):
        registro = Nota.mostrar(ID_usario)
        if len(registro)>0:
            return registro
        else:
            return []
    @staticmethod
    def eliminar_nota(id_nota):
        respuesta = Nota.borrar(id_nota)
        controlador.mensajes_de_confirmacion(respuesta)

    @staticmethod
    def modificar_nota(id,titulo,descripcion):
        respuesta = Nota.cambiar(id,titulo,descripcion)
        controlador.mensajes_de_confirmacion(respuesta)
    
