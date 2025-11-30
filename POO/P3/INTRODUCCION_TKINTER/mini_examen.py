class figuras():
    def __init__(self, valor_x, valor_y, visible):
        self.valor_x = valor_x
        self.valor_y = valor_y
        self.visible = visible

    def get_valor_x(self):
        return self.valor_x
    
    def get_valor_y(self):
        return self.valor_y
    
    def get_visible(self):
        return self.visible
    
    def set_valor_x(self, valor_x):
        self.valor_x = valor_x

    def set_valor_y(self, valor_y):
        self.valor_y = valor_y

    def set_visible(self, visible):
        self.visible = visible

    def esta_visible(self):
        if self.visible:
            print("Esta visible")
            return True
        else:
            print("No esta visible")
            return False

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mover(mover_x, mover_y):
        print(f"La figura se a movido en Y {mover_x} y en Y {mover_y}")

    def calcularArea(self):
        area = self.valor_x * self.valor_y
        return area

class Rentangulos(figuras):
    def __init__(self, valor_x, valor_y, visible, alto, ancho):
        super().__init__(valor_x, valor_y, visible)
        self.__alto = alto 
        self.__ancho = ancho

    def get_alto(self):
        return self.__alto
    
    def get_ancho(self):
        return self.__ancho
    
    def set_alto(self, alto):
        self.__alto = alto

    def set_ancho(self, ancho):
        self.__ancho = ancho

    def ocultar(self):
        self.visible = False
    
    def mostrar(self):
        self.visible = True

    def calcularArea(self):
        area = self.__alto * self.__ancho
        return area
    
class Circulos(figuras):
        def __init__(self, valor_x, valor_y, visible, radio):
            super().__init__(valor_x, valor_y, visible)
            self.__radio = radio

        def get_radio(self):
            return self.__radio
        
        def set_radio(self, radio):
            self.__radio = radio

        def ocultar(self):
            self.visible = False

        def mostrar(self):
            self.visible = True

        def calcularArea(self):
            area = 3.14 * (self.__radio ** 2)
            return area
        
rectangulo1 = Rentangulos(3, 4, True, 10, 20)
circulo1 = Circulos(3, 3, True, 6)