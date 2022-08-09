class Rectangulo:
    def __init__(self, lado_a: float, lado_b: float):
        self.h: float = lado_a
        self.b: float = lado_b

    def calcular_perimetro(self):
        perimetro: float = 2*(self.h + self.b)
        return perimetro

    def calcular_area(self):
        area: float = (self.h * self.b)
        return area

    def cuadrado(self):
        if self.h == self.b:
            print("El rectángulo es cuadrado")
        else:
            print("El rectángulo no es cuadrado")
