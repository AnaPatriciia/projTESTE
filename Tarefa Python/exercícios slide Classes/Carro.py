class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel=5):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel

    def calcular_imposto(self):
        imposto = (self.valor * 3) / 100
        return imposto
    
    def ligar(self):
        print(f"{self.modelo} Ligado!")

    def abastecer(self,qtd_litros):
        self.nivel = self.nivel + qtd_litros

    def andar(self,km):
      consumo = km /10.8
      self.nivel = self.nivel - consumo

    def verificar_nivel(self):
        return self.nivel
    
car1 = Carro("Jetta", "Volks", "Prata",2022,180000)
print(car1.calcular_imposto())
car1.ligar()
print("Nivel de gasolina",car1.nivel,"litros")
car1.abastecer(45)
print("Nivel de gasolina",car1.nivel,"litros")
car1.andar(250)
tanque = car1.verificar_nivel()
print(f"{tanque:.2f}")