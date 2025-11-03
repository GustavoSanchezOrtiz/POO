import mysql.connector

try: 
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_proyecto_coches'
    )
    cursor=conexion.cursor(buffered=True)
except:
    input("ocurrio un error al conectar con la base de datos")

