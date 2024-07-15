from Funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
    
    def calcular_salario(self):
        return self.salario + self.comissao
    
    def bater_meta(self):
        if self.comissao > 1020:  
            return True
        else:
            return False
