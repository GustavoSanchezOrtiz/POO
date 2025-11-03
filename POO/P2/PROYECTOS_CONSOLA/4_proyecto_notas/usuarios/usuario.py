import datetime
from conexionBD import ConexionDB
import hashlib
    
class Usuario:
    def __init__(self, id, nombre, apellidos, email, fecha):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.fecha = fecha

    def registrar_en_BD(self, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            sql="insert into usuarios (nombre, apellidos, email, password, fecha) values (%s, %s, %s, %s, %s)"
            val=(self.nombre,self.apellidos,self.email,contrasena,self.fecha)
            ConexionDB._cursor.execute(sql,val)
            ConexionDB._conexion.commit() 
            return True
        except:
            return False
        
    @staticmethod
    def iniciar_sesion(email,contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            sql="select * from usuarios where email=%s and password=%s"
            val=(email,contrasena)
            ConexionDB._cursor.execute(sql,val)
            registros=ConexionDB._cursor.fetchone()
            if registros:
             return registros
            else:
                return None
        except:
            return None