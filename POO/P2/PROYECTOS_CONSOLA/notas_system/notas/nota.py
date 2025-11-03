from conexionesBD import *


class Notas():
  def __init__(self, usuario_id, titulo, descripcion):
        self.__usuario_id = usuario_id
        self.__titulo = titulo
        self.__descripcion = descripcion

  def get_usuario_id(self):
        return self.__usuario_id
    
  def get_titulo(self):
        return self.__titulo
    
  def get_descripcion(self):
        return self.__descripcion
    
  def set_usuario_id(self, usuario_id):
        self.__usuario_id = usuario_id

  def set_titulo(self, titulo):
        self.__titulo = titulo

  def set_descripcion(self, descripcion):
        self.__descripcion = descripcion 
    
  def insertar_usuario_en_bd(self):
        try:
          ConexionDB._cursor.execute(
            "insert into notas values(null,%s,%s,%s,NOW())",
            (self.__usuario_id,self.__titulo,self.__descripcion)
          )
          ConexionDB._conexion.commit()
          return True
        except:
          return False
    
  def mostrar_usuario_en_bd(self):
        try:
          ConexionDB._cursor.execute(
            "select * from notas where usuario_id=%s",
            (self.__usuario_id,)
          )
          return ConexionDB._cursor.fetchall()
        except:    
          return []
        
  def eliminar_usuario_en_bd(self):
      try:
          ConexionDB._cursor.execute(
            "delete from notas where id=%s",
            (self.__usuario_id,)
          ) 
          ConexionDB._conexion.commit() 
          return True  
      except:    
          return False
      
  def actualizar(self):
       try:
         ConexionDB._cursor.execute(
            "update notas set titulo=%s,descripcion=%s where id=%s",
            (self.__titulo, self.__descripcion, self.__usuario_id)
         )
         ConexionDB._conexion.commit()
         return True
       except: 
         return False