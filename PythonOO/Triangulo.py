class Triangulo:
    def __init__(self,lado_a,lado_b,lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self,lado_a,lado_b,lado_c):
        resultado = lado_a + lado_b + lado_c
        return resultado
    
    def getMaiorlado(self):
        return max(self.lado_a,self.lado_b,self.lado_c)
  
    def calcular_area(self):
        perimetro = self.lado_a + self.lado_b + self.lado_c
        #corrigir aqui

        

lado_a = int(input("Digite o valor do lado a:"))
lado_b= int(input("Digite o valor do lado b:"))
lado_c = int(input("Digite o valor do lado c:"))

triangulo1 = Triangulo(lado_a,lado_b,lado_c)

print(f'perímetro {triangulo1.calcular_perimetro()}')
print(f'maior lado {triangulo1.getMaiorlado()}')
print(f'area {triangulo1.calcular_area()}')

    
    
  