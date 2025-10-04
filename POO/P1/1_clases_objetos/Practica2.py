import os 
os.system("cls")
#crear una clase 
class Coches:
    #metodo contructor que inicializa los atributos cuando se instancia un objeto de la clase 
    def __init__(self,marca,color,velocidad):
        self.marca=marca
        self.color=color
        self.velocidad=velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento
        return self.velocidad 
    
    def frenar(self, decremento):
        self.velocidad= self.velocidad-decremento
        return self.velocidad
    
    def tocar_claxon(self):
        return "pip"
    
#instanciar objetos de la clase coches

Coche1 = Coches("Blanco", "Toyota", 220)
Coche2 = Coches("Amarillo", "Nissan", 180)

print(f" los valores de Coche 1 son: {Coche1.color}, {Coche1.marca}, {Coche1.velocidad}")

print(f"La velocidad original del coche 1 es: {Coche1.velocidad} y cambio a: {Coche1.acelerar(50)}")

print(f" los valores de Coche 2 son: {Coche2.color}, {Coche2.marca}, {Coche2.velocidad}")

print(f"La velocidad de el choche2 antes de frenar es de {Coche2.velocidad} ahora es {Coche2.frenar(100)}")