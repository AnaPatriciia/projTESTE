
class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        print(f"{self.nome} {self.sobrenome}")

    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário: R${salario:.2f}")

    def incrementar_horas(self, horas_adicionais):
        self.horas_trabalhadas += horas_adicionais
        print(f"Total de horas trabalhadas: {self.horas_trabalhadas}")

funcionario = Funcionario("Ana", "Oliveira", 100, 30)
funcionario.nome_completo()        
funcionario.calcular_salario()     
funcionario.incrementar_horas(20) 
funcionario.calcular_salario()      

