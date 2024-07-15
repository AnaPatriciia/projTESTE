class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    
    def maiorLado(self):
        return max(self.ladoA,self.ladoB,self.ladoC)
    
lA = float(input("Digite o valor do lado A: "))
lB= float(input("Digite o valor do lado B: "))
lC = float(input("Digite o valor do lado C: "))

triangulo= Triangulo(lA,lB,lC)

medida =triangulo.calcularPerimetro()
print("O perimetro do triangulo é: ",medida)

lados = triangulo.maiorLado()
print("O maior lado do triangulo é: ",lados)
