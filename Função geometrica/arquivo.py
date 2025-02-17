import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    @staticmethod
    def distancia(p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    @staticmethod
    def distancia_reta(p, a, b):
        x1, y1 = a.x, a.y
        x2, y2 = b.x, b.y

        numerador = abs((y2 - y1) * p.x - (x2 - x1) * p.y + x2 * y1 - y2 * x1)
        denominador = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return numerador / denominador

    @staticmethod
    def area_triangulo(p1, p2, p3):
        return abs(p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2

    @staticmethod
    def area_quadrilatero(p1, p2, p3, p4):
        area1 = Ponto.area_triangulo(p1, p2, p3)
        area2 = Ponto.area_triangulo(p1, p3, p4)
        return area1 + area2
