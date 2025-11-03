from conexionBD import *

class autos:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
      self._marca=marca
      self._color=color
      self._modelo=modelo
      self._velocidad=velocidad
      self._caballaje=caballaje
      self._plazas=plazas

    @staticmethod
    def insertar_en_bd(self):
        try:
            cursor.execute("insert into coches values(null,%s,%s,%s,%s,%s,%s)",(self._color,self._marca,self._modelo,self._velocidad,self._caballaje,self._plazas))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def actualizar_en_bd(Marca, Color, Modelo, Velocidad, Caballaje, Plazas, ID_coches):
        try:
            cursor.execute("update coches set Color=%s, Marca=%s, Modelo=%s, Velocidad=%s, Caballaje=%s, Plazas=%s where ID_coches=%s",(Color, Marca, Modelo, Velocidad, Caballaje, Plazas, ID_coches))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar_en_bd(ID_coches):
        try:
            cursor.execute("delete from coches where ID_coches=%s",(ID_coches,))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar_en_bd():
        try:
            cursor.execute("select * from coches")
            resultados=cursor.fetchall()
            return resultados
        except:
            return []



class camionetas(autos):
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

    @staticmethod
    def insertar_en_bd( color, marca, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            cursor.execute("insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",(color, marca, modelo, velocidad, caballaje, plazas, traccion, cerrada))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def actualizar_en_bd(Marca, Color, Modelo, Velocidad, Caballaje, Plazas, Traccion, Cerrada, ID_Camionetas):
        try:
            cursor.execute("update camionetas set Color=%s, Marca=%s, Modelo=%s, Velocidad=%s, Caballaje=%s, Plazas=%s, Traccion=%s, Cerrada=%s where ID_Camioneta=%s",(Color, Marca, Modelo, Velocidad, Caballaje, Plazas, Traccion, Cerrada, ID_Camionetas))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod 
    def eliminar_en_bd(ID_Camionetas):
        try:
            cursor.execute("delete from camionetas where ID_Camioneta=%s",(ID_Camionetas,))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar_en_bd():
        try:
            cursor.execute("select * from camionetas")
            resultados=cursor.fetchall()
            return resultados
        except:
            return []

class camiones(autos):
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    @staticmethod
    def insertar_en_bd(color, marca, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        try:
            cursor.execute("insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",(color, marca, modelo, velocidad, caballaje, plazas, eje, capacidadCarga))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def actualizar_en_bd(Marca, Color, Modelo, Velocidad, Caballaje, Plazas, Eje, Capacidad_de_carga, id):
        try:
            cursor.execute("update camiones set Color=%s, Marca=%s, Modelo=%s, Velocidad=%s, Caballaje=%s, Plazas=%s, Eje=%s, Capacidad_de_Carga=%s where ID_Camiones=%s",(Color, Marca, Modelo, Velocidad, Caballaje, Plazas, Eje, Capacidad_de_carga, id))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar_en_bd(ID_Camiones):    
        try:
            cursor.execute("delete from camiones where ID_Camiones=%s",(ID_Camiones,))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar_en_bd():
        try:
            cursor.execute("select * from camiones")
            resultados=cursor.fetchall()
            return resultados
        except:
            return []
