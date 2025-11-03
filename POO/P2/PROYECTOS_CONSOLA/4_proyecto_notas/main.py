
from datetime import datetime
import getpass

from funciones import funciones_basicas as FB        
from usuarios.usuario import Usuario                 
from notas.nota import Nota                          
from conexionBD import ConexionDB                    

class AppNotas:
    def __init__(self):
        
        ConexionDB.obtener_conexion()  
        self._running = True

    def run(self):
        while self._running:
            FB.borrarPantalla()
            opcion = FB.menu_usuarios()

            if opcion in ("1", "REGISTRO"):
                self.registrar_usuario()

            elif opcion in ("2", "LOGIN"):
                usuario = self.login()
                if usuario:
                    self.menu_notas(usuario)

            elif opcion in ("3", "SALIR"):
                print("Termino la Ejecución del Sistema")
                self._running = False
                FB.esperarTecla()

            else:
                print("Opción no válida")
                FB.esperarTecla()

    def registrar_usuario(self):
        FB.borrarPantalla()
        print("\n \t ..:: Registro en el Sistema ::..")

        nombre    = input("\t ¿Cuál es tu nombre?: ").upper().strip()
        apellidos = input("\t ¿Cuáles son tus apellidos?: ").upper().strip()
        email     = input("\t Ingresa tu email: ").lower().strip()
        password  = getpass.getpass("\t Ingresa tu contraseña: ").strip()

        usuario = Usuario(
            id=None,
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            fecha=datetime.now()
        )
        if usuario.registrar_en_BD(password):
            print(f"\n\t {nombre} {apellidos}, se registró correctamente con el email: {email}")
        else:
            print("\n\t ...Por favor inténtalo de nuevo, no fue posible registrar al usuario")
        FB.esperarTecla()

    def login(self):
        FB.borrarPantalla()
        print("\n \t ..:: Inicio de Sesión ::.. ")

        email    = input("\t Ingresa tu E-mail: ").lower().strip()
        password = getpass.getpass("\t Ingresa tu contraseña: ").strip()

        registro = Usuario.iniciar_sesion(email, password)

        if registro:
            usuario = Usuario(
                id=registro[0],
                nombre=registro[1],
                apellidos=registro[2],
                email=registro[3],
                fecha=registro[5] if len(registro) > 5 else None
            )
            return usuario
        else:
            print("\n\t E-mail y/o contraseña incorrectos, vuelve a intentarlo...")
            FB.esperarTecla()
            return None

    def menu_notas(self, usuario: Usuario):
        while True:
            FB.borrarPantalla()
            print(f"\n \t \t \t Bienvenido {usuario.nombre} {usuario.apellidos}, has iniciado sesión ...")
            opcion = FB.menu_notas()

            if opcion in ('1', 'CREAR'):
                self.crear_nota(usuario)

            elif opcion in ('2', 'MOSTRAR'):
                self.mostrar_notas(usuario)

            elif opcion in ('3', 'CAMBIAR'):
                self.actualizar_nota(usuario)

            elif opcion in ('4', 'ELIMINAR'):
                self.eliminar_nota(usuario)

            elif opcion in ('5', 'SALIR'):
                break

            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                FB.esperarTecla()


    def crear_nota(self, usuario: Usuario):
        FB.borrarPantalla()
        print("\n \t .:: Crear Nota ::. ")
        titulo = input("\tTítulo: ")
        descripcion = input("\tDescripción: ")

        nota = Nota(id=None, usuario_id=usuario.id, titulo=titulo, descripcion=descripcion, fecha=None)
        if nota.insertar_en_BD():
            print(f"\n\t\tSe creó la nota: {titulo} exitosamente")
        else:
            print("\n\t\tNo fue posible crear la nota en este momento, vuelve a intentar...")
        FB.esperarTecla()

    def mostrar_notas(self, usuario: Usuario):
        FB.borrarPantalla()
        consulta = Nota(id=None, usuario_id=usuario.id, titulo="", descripcion="", fecha=None)
        filas = consulta.mostrar_notas_usuario()
        if filas:
            print(f"\n\tMostrar notas")
            print(f"{'ID':<10}{'titulo':<15}{'descripcion':<15}{'fecha':<15}")
            print("-" * 80)
            for f in filas:
                print(f"{f[0]:<10}{f[2]:<15}{f[3]:<15}{f[4]}")
            print("-" * 80)
        else:
            print("\n\t No existen notas de acuerdo al usuario")
        FB.esperarTecla()

    def actualizar_nota(self, usuario: Usuario):
        FB.borrarPantalla()
        print(f"\n \t .:: {usuario.nombre} {usuario.apellidos}, vamos a modificar una Nota ::. \n")
        self.mostrar_notas(usuario)

        id_str = input("\t \t ID de la nota a actualizar: ").strip()
        titulo = input("\t Nuevo título: ")
        descripcion = input("\t Nueva descripción: ")

        nota = Nota(id=id_str, usuario_id=usuario.id, titulo=titulo, descripcion=descripcion, fecha=None)
        if nota.actualizar_nota():
            print(f"\n\t\t Se actualizó la nota: {titulo} exitosamente")
        else:
            print("\n\t\t No fue posible actualizar la nota en este momento...")
        FB.esperarTecla()

    def eliminar_nota(self, usuario: Usuario):
        FB.borrarPantalla()
        print(f"\n \t .:: {usuario.nombre} {usuario.apellidos}, vamos a borrar una Nota ::. \n")
        self.mostrar_notas(usuario)

        id_str = input("\t \t ID de la nota a eliminar: ").strip()
        nota = Nota(id=id_str, usuario_id=usuario.id, titulo="", descripcion="", fecha=None)
        if nota.borrar_nota():
            print("\n\t\tSe borró la nota exitosamente")
        else:
            print("\n\t\t No fue posible borrar la nota")
        FB.esperarTecla()


if __name__ == "__main__":
    AppNotas().run()
