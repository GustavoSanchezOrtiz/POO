import os 
os.system("cls")


class clase():
    atributo_publivo="Soy un atributo publico"
    _atributo_protegido= "Soy un atributo protegido"
    __atributo_privado="soy un atributo privado"

    def __init__(self, color, tamano, ):
        self.__color = color
        self.__tamano = tamano 

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color 

    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano
    
    def get_atributo_privado(self):
        return self.__atributo_privado
    
    def set_atributo_privado(self, atributo_privado):
        self.__atributo_privado = atributo_privado

#usar los atributos y metodos de acuerdo a su encapsulamiento
objeto = clase("rojo", "grande")
print(f"mi objeto tiene los siguientes valores: {objeto.color}, y {objeto.tamano}")

print(f"soy  el contenido del atributo: {objeto.atributo_publivo}")
print(f"soy  el contenido del atributo: {objeto._atributo_protegido}")
print(f"soy  el contenido del atributo: {objeto.get_atributo_privado()}")

objeto.set_atributo_privado(f"se ha cambiaddo el valor del atributo privado")
print(f"soy  el contenido del atributo: {objeto.get_atributo_privado()}")


