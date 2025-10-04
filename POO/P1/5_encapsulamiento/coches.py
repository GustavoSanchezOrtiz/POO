# NO USAR METODO CONSTRUCTOR, TODOS LOS ATRIBUTOS SON PUIBLICOS, METODOS DE ACELERAR Y FRENAR NO HACE NADA .
'''import os 
os.system("cls")

class Coches():
    Marca=""
    Color=""
    Modelo=""
    Velocidad=0
    Caballaje=0 
    Plazas=0

    def acelerar():
        pass

    def frenar():
        pass

Coche1=Coches()
Coche1.Marca = "VW"
Coche1.Color = "Blanco"
Coche1.Modelo = "2020"
Coche1.Velocidad = 220
Coche1.Caballaje = 150
Coche1.Plazas = 5 


Coche2=Coches()
Coche2.Marca = "Nissan"
Coche2.Color = "Azul"
Coche2.Modelo = "2020"
Coche2.Velocidad = 180
Coche2.Caballaje = 150
Coche2.Plazas = 6

print(
Coche1.Marca, 
Coche1.Color,
Coche1.Modelo,
Coche1.Velocidad,
Coche1.Caballaje,
Coche1.Plazas)

print(
Coche2.Marca, 
Coche2.Color,
Coche2.Modelo,
Coche2.Velocidad,
Coche2.Caballaje,
Coche2.Plazas)
'''
import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
    
      self.__marca = marca
      self.__color= color 
      self.__modelo=modelo
      self.__velocidad=velocidad
      self.__caballaje=caballaje
      self.__plazas=plazas

    numero_de_serie = ""
    #crear los metodos get y set para cada atributo estos metodos son importantes y necesarios en todas las clases que el programador creee para poder interactuar con los valores de los atributos a traves de estos metodos digamos que son la manera mas adecuada para solicitar un valor (get) o para modificar un valor (set) a un atributo en particular de la clase a traves de un objeto
    # en teoria se debe de crear un metodo get y set para cada atributo de la clase
    #los metodos get y set siempre regresan un valor es decir el valor de la propiedad a traves del return
    #por otro lado los metodos set no regresan ningun valor pero si reciben un parametro que es el valor que se le va a asignar a la propiedad
    #Metodos o acciones o funciones que hace el objeto 

    #1er forma
    def get_marca(self):
      return self.__marca
    
    def set_marca(self, marca):
      self.__marca = marca

    #propierty 2da forma 

    @property
    def marca2(self):
      return self.__marca
    
    @marca2.setter
    def marca2(self, marca):
      self.__marca = marca

    def get_color(self):
      return self.__color
    
    def set_color(self, color):
      self.__color = color

    def get_modelo(self):
      return self.__modelo
    
    def set_modelo(self, modelo):
      self.__modelo = modelo

    def get_velocidad(self):
      return self.__velocidad
    
    def set_velocidad(self, velocidad):
      self.__velocidad = velocidad

    def get_caballaje(self):
      return self.__caballaje
    
    def set_caballaje(self, caballaje):
      self.__caballaje = caballaje
    
    def get_plazas(self):
      return self.__plazas
    
    def set_plazas(self, plazas):
      self.__plazas = plazas

    def acelerar(self):
      return "estas acelarando"

    def frenar(self):
      return "estas frenando"

#Fin definir clase

#Crear un objetos o instanciar la clase



'''coche1.set_marca("VW")
coche1.set_color("blanco")
coche1.set_modelo("2022")
coche1.set_velocidad(220)
coche1.set_caballaje(150)
coche1.set_plazas(5)'''


'''coche2.set_marca("nissan")
coche2.set_color("azul")
coche2.set_modelo("2020")
coche2.set_velocidad(180)
coche2.set_caballaje(150)
coche2.set_plazas(6)'''



'''
coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

print(f"Datos del Vehiculo: \n Marca:{coche1.marca} \n color: {coche1.color} \n Modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje: {coche1.caballaje} \n plazas: {coche1.plazas} ")

coche2=Coches()

coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"\nDatos del Vehiculo: \n Marca:{coche2.marca} \n color: {coche2.color} \n Modelo: {coche2.modelo} \n velocidad: {coche2.velocidad} \n caballaje: {coche2.caballaje} \n plazas: {coche2.plazas} ")

'''

