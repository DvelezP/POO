import math


class Punto:
    def __init__(self, coordenada_x: int, coordenada_y: int):
        self.x: int = coordenada_x
        self.y: int = coordenada_y

    def mostrar(self):
        print(f"({self.x}, {self.y})")

    def mover(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto):
        c1: float = self.y - otro_punto.y
        c2: float = self.x - otro_punto.x
        distancia: float = math.sqrt(c1**2 + c2**2)
        return distancia


