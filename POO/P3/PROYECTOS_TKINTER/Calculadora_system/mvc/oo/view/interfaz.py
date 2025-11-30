from tkinter import messagebox
import tkinter as tk
from controller import funciones
from model import operaciones_basicas

#Interfaz o VIEW
class vista():
    def __init__(self,ventana):
        ventana.title("calculadora basica")
        ventana.geometry("600x600")
        ventana.resizable(False, False)
        self.Interfaz(ventana)

    def menu(self, ventana):
        menuBar = tk.Menu(ventana)
        ventana.config(menu=menuBar)
        operacionMenu = tk.Menu(menuBar , tearoff=1)
        menuBar.add_cascade(label="Operacion" , menu=operacionMenu)
        operacionMenu.add_command(label="Agregar", command=lambda:self.Interfaz(ventana))
        operacionMenu.add_command(label="Consultar", command=lambda:self.interfaz_ListaOperaciones(ventana))
        operacionMenu.add_command(label="Cambiar", command=lambda:self.interfaz_actualizar_operaciones(ventana))
        operacionMenu.add_command(label="Eliminar", command=lambda:self.interfaz_elimar_entrada())
        operacionMenu.add_separator()
        operacionMenu.add_command(label="Salir",command=ventana.quit)
        
    def Interfaz(self, ventana):
        funciones.Funciones.borrar_pantalla(ventana)
        var_num1 = tk.IntVar() 
        var_num2 = tk.IntVar()

        self.menu(ventana)

        
        var_entrada_n1 = tk.Entry(ventana, textvariable=var_num1, justify="right")
        var_entrada_n1.pack()

        var_entrada_n2 = tk.Entry(ventana, textvariable=var_num2, justify="right")
        var_entrada_n2.pack()

        btn_sumar=tk.Button(ventana,text="+",command=lambda:funciones.Funciones.operacion("+",var_num1.get(),var_num2.get()))
        btn_sumar.pack()
        btn_restar=tk.Button(ventana,text="-",command=lambda:funciones.Funciones.operacion("-",var_num1.get(),var_num2.get()))
        btn_restar.pack()
        btn_multiplicar=tk.Button(ventana,text="X",command=lambda:funciones.Funciones.operacion("X",var_num1.get(),var_num2.get()))
        btn_multiplicar.pack()
        btn_dividir=tk.Button(ventana,text="/",command=lambda:funciones.Funciones.operacion("/",var_num1.get(),var_num2.get()))
        btn_dividir.pack()

        btn_salir = tk.Button(ventana, text="Salir", command=quit)
        btn_salir.pack()
        var_entrada_n1.focus_set()

    def interfaz_elimar_entrada(self):
        ventana_eliminar = tk.Toplevel()
        ventana_eliminar.title("Eliminar Entrada")
        ventana_eliminar.geometry("400x200")
        ventana_eliminar.resizable(False, False)

        

        lbl_Titulo_OperacionAEliminar = tk.Label(ventana_eliminar, text=".:: Borrar Operacion ::.", font=("Arial", 16))
        lbl_Titulo_OperacionAEliminar.pack(pady=10)

        lbl_Indicacion_IngreseID = tk.Label(ventana_eliminar, text="Ingrese el ID de la operacion a eliminar:")
        lbl_Indicacion_IngreseID.pack()

        var_ID_OperacionAEliminar = tk.IntVar()
        entry_ID_OperacionAEliminar = tk.Entry(ventana_eliminar, textvariable=var_ID_OperacionAEliminar)
        entry_ID_OperacionAEliminar.pack()
        btn_Eliminar_Operacion = tk.Button(ventana_eliminar, text="Eliminar", command=lambda: funciones.Funciones.eliminacion_en_bd(var_ID_OperacionAEliminar.get()))
        btn_Eliminar_Operacion.pack(pady=10)

        btn_voler_atras = tk.Button(ventana_eliminar, text="Volver Atrás", command=ventana_eliminar.destroy)
        btn_voler_atras.pack()
        entry_ID_OperacionAEliminar.focus()

        ventana_eliminar.grab_set()  
        ventana_eliminar.wait_window()

    def interfaz_ListaOperaciones(self, ventana):
        funciones.Funciones.borrar_pantalla(ventana)
        self.menu(ventana)
        lbl_Titulo_ListaOperaciones = tk.Label(ventana, text=".:: Listado de operaciones ::.", font=("Arial", 16))
        lbl_Titulo_ListaOperaciones.pack(pady=10)
        lista_de_operaciones_en_bd = operaciones_basicas.OperacionesBD.obtener_operaciones()
        if len (lista_de_operaciones_en_bd) > 0:
            num= 0
            for i in lista_de_operaciones_en_bd:
                num = num +1
                lbl_Operacion = tk.Label(ventana, text=f"Operacion = {num} ID: {i[0]}  Fecha de creacion : {i[1]} \n Operación =  {i[2]} {i[4]} {i[3]} = {i[5]}")
                lbl_Operacion.pack()
        else:
            lbl_SinOperaciones = tk.Label(ventana, text="No hay operaciones guardadas en la base de datos.")
            lbl_SinOperaciones.pack()
        btn_volver_InterfazPrincipal = tk.Button(ventana, text="Volver", command=lambda: self.Interfaz(ventana))
        btn_volver_InterfazPrincipal.pack()

    def ocurrio_error(self):
        messagebox.showerror("Ocurrio un error inesperado", icon="error")

    def interfaz_actualizar_operaciones(self, ventana):
        funciones.Funciones.borrar_pantalla(ventana)
        
        lbl_1=tk.Label(ventana,text=".:: Cambiar una Operacion ::.")
        lbl_1.pack()
        
        lbl_id=tk.Label(ventana,text="ID de la operación: ")
        lbl_id.pack()
        id=tk.IntVar()
        txt_id=tk.Entry(ventana,textvariable=id,width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        btn_cambiar_a_segunda_interfaz = tk.Button(
            ventana,text="Modificar", command= lambda: self.cambio_a_segunda_interfaz_comandos(id.get(), ventana)
        )
        btn_cambiar_a_segunda_interfaz.pack(pady= 5)

    def cambio_a_segunda_interfaz_comandos(self, id, ventana):
        operacion_en_bd = operaciones_basicas.OperacionesBD.obtener_operacion_especifica(id)
        if len(operacion_en_bd)>0:
            operacion_en_bd1 = operacion_en_bd[0]
            self.segunda_interfaz_de_actualizar_operaciones(ventana, operacion_en_bd1)
        else:
            messagebox.showerror(title="No existe ese id en la BD", message=f"La operacion que buscas con id: {id} no existe en la bd")
        
        

    def segunda_interfaz_de_actualizar_operaciones(self, ventana, operacion_en_bd):
        funciones.Funciones.borrar_pantalla(ventana)
        ID_operacion = operacion_en_bd[0]
        n1_operacion_a_cambiar = operacion_en_bd[2]
        signo_operacion_a_cambiar = operacion_en_bd[4]
        n2_operacion_a_cambiar = operacion_en_bd[3]
        resultado_operacion_a_cambiar = operacion_en_bd[5]
        lbl_1=tk.Label(ventana,text=".:: Cambiar una Operacion ::.")
        lbl_1.pack()
        
        lbl_id=tk.Label(ventana,text="ID de la operación: ")
        lbl_id.pack()
        id=tk.StringVar()
        txt_id=tk.Entry(ventana,textvariable=id,width=5)
        txt_id.insert(0, ID_operacion)
        txt_id.config(state="readonly")
        txt_id.focus()
        txt_id.pack(pady=5)

        n1=tk.StringVar()
        n2=tk.StringVar()
        lbl_num1=tk.Label(ventana,text="Nuevo numero 1: ")
        lbl_num1.pack()
        numero1=tk.Entry(ventana,textvariable=n1,width=10,justify="right")
        numero1.insert(0, n1_operacion_a_cambiar)
        numero1.focus()
        numero1.pack(side="top",anchor="center")
        
        lbl_num2=tk.Label(ventana,text="Nuevo numero 2: ")
        lbl_num2.pack()     
        numero2=tk.Entry(ventana,textvariable=n2,width=10,justify="right")
        numero2.insert(0, n2_operacion_a_cambiar)
        numero2.pack(side="top",anchor="center")
        
        lbl_signo=tk.Label(ventana,text="Nuevo Signo: ")
        lbl_signo.pack()
        signo=tk.StringVar()
        nuevo_signo=tk.Entry(ventana,textvariable=signo,width=10,justify="center")
        nuevo_signo.insert(0, signo_operacion_a_cambiar)
        nuevo_signo.pack()
        
        lbl_resultado=tk.Label(ventana,text="Nuevo resultado: ")
        lbl_resultado.pack()
        
        resultado=tk.StringVar()
        nuevo_resultado=tk.Entry(ventana,textvariable=resultado,width=10,justify="right")
        nuevo_resultado.insert(0, resultado_operacion_a_cambiar)
        nuevo_resultado.pack()
        
        btn_guardar=tk.Button(ventana,text="Guardar",command=lambda: {vista.guardar_operacion_en_bd(
            id.get(),
            n1.get(),
            n2.get(),
            signo.get(),
            resultado.get()
        ), self.Interfaz(ventana)})
        btn_guardar.pack()
        
        btn_volver=tk.Button(ventana,text="Volver",command=lambda: self.Interfaz(ventana))
        btn_volver.pack()

    @staticmethod
    def guardar_operacion_en_bd(id, n1, n2, signo, resultado):
        confirmacion = messagebox.askquestion("",f"¿Estas seguro de que desear sustitur la operacion {id}: {n1} {signo} {n2} = {resultado} en la base de datos", icon="info")
        if confirmacion == "yes":
            var_confirmacion = operaciones_basicas.OperacionesBD.actualizar_operacion(id, n1, n2, signo, resultado)
            if var_confirmacion:
                messagebox.showinfo("Confirmacion","Se guardo correctamente en la base de datos", icon="info")
            else:
                messagebox.showerror("ocurrio un error en la base de datos","Ocurrio un error al intentar guadar en la BD", icon="error")


    
    
    