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
os.system("clear")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

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