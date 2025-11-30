'''
    crear una calculadora :
    1.- Dos campos de textos
    2.- 4 botones para las operaciones 
    3.- Mostrar el resultado en una alerta
    4.- programado de forma Orientado a objetos(OO)
    5.- considerar el MVC
'''


import conexionBD
from view import interfaz
import tkinter as tk

class App():
    @staticmethod
    def inicializador(ventana):
        view = interfaz.vista(ventana)
        conexionBD.ConexionDB.obtener_conexion()
       


if __name__=="__main__":
    ventana = tk.Tk()
    app=App.inicializador(ventana)
    ventana.mainloop()

