import mysql.connector 
from conexionBD import ConexionDB

class OperacionesBD:
    @staticmethod
    def insertar_en_bd(numero1, numero2, signo, resultado):
        try:
            sql = "INSERT INTO operaciones VALUES(null,NOW(),%s,%s,%s,%s)"
            val = (numero1, numero2, signo, resultado)
            ConexionDB._cursor.execute(sql, val)
            ConexionDB._conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def obtener_operaciones():
        try:
            sql = "SELECT * FROM operaciones"
            ConexionDB._cursor.execute(sql)
            return ConexionDB._cursor.fetchall()
        except:
            return []

    @staticmethod
    def obtener_operacion_especifica(id):
        try:
            sql = "SELECT * FROM operaciones where ID_operacion= %s"
            val = (id,)
            ConexionDB._cursor.execute(sql, val)
            return ConexionDB._cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def borrar_operaciones(id):
        try:
            sql = "DELETE FROM operaciones WHERE ID_operacion=%s"
            val = (id,)
            ConexionDB._cursor.execute(sql, val)
            ConexionDB._conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def actualizar_operacion(id, numero1, numero2, signo, resultado):
        try:
            sql = "UPDATE operaciones SET numero1=%s, numero2=%s, signo=%s, resultado=%s WHERE ID_operacion=%s"
            val = (numero1, numero2, signo, resultado, id)
            ConexionDB._cursor.execute(sql, val)
            ConexionDB._conexion.commit()
            return True
        except:
            return False