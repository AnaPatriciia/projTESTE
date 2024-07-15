from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha
    
    def calcular_salario(self):
        return self.salario + 1000  
    
    def aprovar_folga(self):
        return f"Folga aprovada para: {self.nome}."
