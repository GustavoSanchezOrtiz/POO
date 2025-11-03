import mysql.connector

class ConexionDB:
    _conexion = None   # guardará la conexión
    _cursor = None     # guardará el cursor

    @classmethod
    def obtener_conexion(cls):
        # Si no hay conexión, se crea
        if cls._conexion is None:
            try:
                cls._conexion = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="",
                    database="bd_notas",
                    port=3307
                )
                cls._cursor = cls._conexion.cursor(buffered=True)
                print("Conexión y cursor creados con éxito.")
            except:
                print("No es posible conectarse a la base de datos.")
        return cls._conexion, cls._cursor
        


