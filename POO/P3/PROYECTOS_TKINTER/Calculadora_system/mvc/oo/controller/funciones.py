from tkinter import messagebox
from model.operaciones_basicas import OperacionesBD

#Control App o Controller
class Funciones():
    @staticmethod
    def operacion(tipo,numero1,numero2):
        if tipo=="+":
            res=numero1+numero2
            op="+"
        elif tipo=="-":
            res=numero1-numero2
            op="-"
        elif tipo=="X":
            res=numero1*numero2
            op="X"
        elif tipo=="/":
            res=numero1/numero2
            op="/"
        resultado = messagebox.askquestion(title=tipo,message=f"{numero1} {op} {numero2} = {res}\n\n ¿Deseas guardar en la base de datos?",icon="question")
        if resultado=="yes":
            guardado=OperacionesBD.insertar_en_bd(numero1,numero2,op,res)
            if guardado:
                messagebox.showinfo(title="Guardado",message="Operacion guardada en la base de datos",icon="info")
            else:
                messagebox.showerror(title="Error",message="No se pudo guardar la operacion en la base de datos",icon="error")

    @staticmethod
    def eliminacion_en_bd(id):
        try:
            if not id:
                messagebox.showwarning("ID vacío", "Por favor ingresa un ID válido.")
                return

            resultado = messagebox.askyesno(
                "Eliminar Operación",
                f"¿Está seguro de que desea eliminar la operación con ID {id}?"
            )

            if resultado:  
                eliminada = OperacionesBD.borrar_operaciones(id)

                if eliminada:
                    messagebox.showinfo(
                        "Operación eliminada",
                        f"La operación con ID {id} ha sido eliminada."
                    )
                else:
                    messagebox.showwarning(
                        "No se eliminó",
                        f"No se encontró ninguna operación con el ID {id}."
                    )
        except Exception as e:
            messagebox.showerror(
                "Error al eliminar la operación",
                f"Ocurrió un error al eliminar la operación: {e}"
            )

    @staticmethod
    def borrar_pantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()