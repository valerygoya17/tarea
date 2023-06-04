import math
from figurageometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, base: float = 0.0, altura: float = 0.0):
        super().__init__(alto=altura)
        self.base = base

    def __str__(self):
        return f'Triángulo [base = {self.base}, altura = {self.alto}]'

    def calcular_area(self):
        return 0.5 * self.base * self.alto

    def calcular_perimetro(self):
        return self.base + 2 * math.sqrt((self.base / 2) ** 2 + self.alto ** 2)

if __name__ == '__main__':
    tri1 = Triangulo(base=6, altura=4)
    print(tri1)
    print(f'El área del Triángulo es: {tri1.calcular_area()}')
    print(f'El perímetro del Triángulo es: {tri1.calcular_perimetro()}')gitgit