class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def valor_raio(self):
        print(f"Valor do raio é {self.raio}")


    def area_circulo(self):
        area =3.14 * (self.raio ** 2)
        return area

    def circunferencia(self):
        circunferencia = 2 *3.14* self.raio
        return circunferencia

circulo = Circulo(5)
circulo.valor_raio()
print(f"A área do círculo é: {circulo.area_circulo()}")
print(f"A circunferência do círculo é: {circulo.circunferencia()}")




        