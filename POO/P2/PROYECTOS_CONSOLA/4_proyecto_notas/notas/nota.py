from conexionBD import ConexionDB
class Nota:
    def __init__(self, id, usuario_id, titulo, descripcion, fecha):
        self.id = id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha

    def insertar_en_BD(self):
        try:
            sql="insert into notas(usuario_id,titulo,descripcion,fecha) values (%s, %s, %s,NOW())"
            val=(self.usuario_id, self.titulo,self.descripcion)
            ConexionDB._cursor.execute(sql,val)
            ConexionDB._conexion.commit()
            return True
        except:
            return False
        
    def mostrar_notas_usuario(self):
        try:
            sql="select * from notas where usuario_id = %s"
            val=(self.usuario_id,)
            ConexionDB._cursor.execute(sql,val)
            return ConexionDB._cursor.fetchall()
        except:
            return []
        
    def actualizar_nota(self):
        try:
            sql="update notas set titulo=%s, descripcion=%s, fecha=NOW() where id=%s and usuario_id=%s"
            val=(self.titulo, self.descripcion, self.id, self.usuario_id)
            ConexionDB._cursor.execute(sql,val)
            ConexionDB._conexion.commit()
            return True
        except:
            return False
        
    def borrar_nota(self):
        try:
            sql="delete from notas where id=%s and usuario_id=%s"
            val=(self.id, self.usuario_id)
            ConexionDB._cursor.execute(sql,val)
            ConexionDB._conexion.commit()
            return True
        except:
            return False