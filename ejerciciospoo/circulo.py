import math


class Circulo:
    def __init__(self, centro_x: float, centro_y, radio: float):
        self.cx: float = centro_x
        self.cy: float = centro_y
        self.r: float = radio

    def calcular_area(self):
        area = math.pi * self.r**2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi *self.r
        return perimetro




