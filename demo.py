class Cuadrado:
    def __init__(self, lado):
        self.lado = lado  

    def area(self):
        return self.lado * self.lado
cuadrado = Cuadrado(4)
print("El área del cuadrado es:", cuadrado.area())
