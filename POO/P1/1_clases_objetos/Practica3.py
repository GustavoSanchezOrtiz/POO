import os 
os.system("cls")

class Alumno():
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad

    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, matricula):
        self.matricula = matricula

    def inscribirse(self):
        print(f"{self.nombre} se ha inscrito correctamente.")
    
    def estudiar(self):
        print(f"{self.nombre} ha estudiado x horas")

class Profesor():
    def __init__(self, nombre, experiencia, num_profesor):
        self.nombre = nombre
        self.experiencia = experiencia
        self.num_profesor = num_profesor
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_experiencia(self):
        return self.experiencia
    
    def set_experiencia(self, experiencia):
        self.experiencia = experiencia

    def get_num_profesor(self):
        return self.num_profesor
    
    def set_num_profesor(self, num_profesor):
        self.num_profesor = num_profesor

    def impartir(self):
        print(f"{self.nombre} ha impartido una clase.")

    def evaluar(self):
        print(f"{self.nombre} ha evaluado a los alumnos.")

class curso():
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_codigo(self):
        return self.codigo
    
    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_creditos(self):
        return self.creditos
    
    def set_creditos(self, creditos):
        self.creditos = creditos

    def asignar(self):
        print(f"El curso {self.nombre} ha sido asignado.")

alumno1 = Alumno("Juana Perez", 18, "314214534")
alumno2 = Alumno("Juan Ramos", 19, "314214535")

profesor1 = Profesor("Dagoberto", 20, "6181559209")
profesor2 = Profesor("Carlos Trejo", 32, "61467128701")

curso1 = curso("Progrmacion_estructurada", "XYzvt56", 6)
curso2 = curso("POO", "VItu889", 10)

