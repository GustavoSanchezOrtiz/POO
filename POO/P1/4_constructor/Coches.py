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
    
      self.marca = marca
      self.color= color 
      self.modelo=modelo
      self.velocidad=velocidad
      self.caballaje=caballaje
      self.plazas=plazas

    numero_de_serie = ""
    #crear los metodos get y set para cada atributo estos metodos son importantes y necesarios en todas las clases que el programador creee para poder interactuar con los valores de los atributos a traves de estos metodos digamos que son la manera mas adecuada para solicitar un valor (get) o para modificar un valor (set) a un atributo en particular de la clase a traves de un objeto
    # en teoria se debe de crear un metodo get y set para cada atributo de la clase
    #los metodos get y set siempre regresan un valor es decir el valor de la propiedad a traves del return
    #por otro lado los metodos set no regresan ningun valor pero si reciben un parametro que es el valor que se le va a asignar a la propiedad
    #Metodos o acciones o funciones que hace el objeto 

    #1er forma
    def get_marca(self):
      return self.marca
    
    def set_marca(self, marca):
      self.marca = marca

    #propierty 2da forma 

    @property
    def marca2(self):
      return self.marca
    
    @marca2.setter
    def marca2(self, marca):
      self.marca = marca

    def get_color(self):
      return self.color
    
    def set_color(self, color):
      self.color = color

    def get_modelo(self):
      return self.modelo
    
    def set_modelo(self, modelo):
      self.modelo = modelo

    def get_velocidad(self):
      return self.velocidad
    
    def set_velocidad(self, velocidad):
      self.velocidad = velocidad

    def get_caballaje(self):
      return self.caballaje
    
    def set_caballaje(self, caballaje):
      self.caballaje = caballaje
    
    def get_plazas(self):
      return self.plazas
    
    def set_plazas(self, plazas):
      self.plazas = plazas

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches("VW", "blanco", "2022", 220, 150, 5)
coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3= Coches("Honda","","",0,0,0)
coche4= Coches("","","",0,0,0)
coche4.marca2 = "volvo"

'''coche1.set_marca("VW")
coche1.set_color("blanco")
coche1.set_modelo("2022")
coche1.set_velocidad(220)
coche1.set_caballaje(150)
coche1.set_plazas(5)'''
coche1.numero_de_serie="B18926"

'''coche2.set_marca("nissan")
coche2.set_color("azul")
coche2.set_modelo("2020")
coche2.set_velocidad(180)
coche2.set_caballaje(150)
coche2.set_plazas(6)'''

print(f"Datos del Vehiculo: 1 \n Marca:{coche1.get_marca()} \n color: {coche1.get_color()} \n Modelo: {coche1.get_modelo()} \n velocidad: {coche1.get_velocidad()} \n caballaje: {coche1.get_caballaje()} \n plazas: {coche1.get_plazas()} \n numero de serie {coche1.numero_de_serie} ")

print(f"Datos del Vehiculo: 2\n Marca:{coche2.get_marca()} \n color: {coche2.get_color()} \n Modelo: {coche2.get_modelo()} \n velocidad: {coche2.get_velocidad()} \n caballaje: {coche2.get_caballaje()} \n plazas: {coche2.get_plazas()} ")



print(f"la marca del 3 es {coche3.marca}")



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

