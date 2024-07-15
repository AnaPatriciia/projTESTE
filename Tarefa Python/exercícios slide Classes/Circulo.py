class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14  

    def imprimirRaio(self):
        print("O raio do círculo é:", self.raio)

    def calcularArea(self):
        area = self.pi * self.raio ** 2
        return area

    def calcularCircunferencia(self):
        circunferencia = 2 * self.pi * self.raio
        return circunferencia


circulo1 = Circulo(5)

circulo1.imprimirRaio()

area = circulo1.calcularArea()
print("Área do círculo:", area)

circunferencia = circulo1.calcularCircunferencia()
print("Circunferência do círculo:", circunferencia)



        