from Pessoa1 import Pessoa1

class Aluno(Pessoa1):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = self.calcular_media()

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0
    
    def estudar(self):
        return f"{self.nome} está estudando."