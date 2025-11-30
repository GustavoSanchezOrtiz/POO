import mysql.connector 

class ConexionDB:
    _conexion = None   
    _cursor = None     
    @classmethod
    def obtener_conexion(cls):
        
        if cls._conexion is None:
            try:
                cls._conexion = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="admin",
                    database="bd_operaciones_basicas",
                    port=3306
                )
                cls._cursor = cls._conexion.cursor(buffered=True)
                print("Conexión y cursor creados con éxito.")
            except:
                print("No es posible conectarse a la base de datos.")
        return cls._conexion, cls._cursor
        


