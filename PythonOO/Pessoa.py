#exercicio 1
class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.idade =idade
        self.nome =nome
        self.endereco = endereco

    def getNome(self):
       return self.nome
    def setIdade(self,novaIdade):
       self.idade = novaIdade
    def geteEndereco(self):
       return self.endereco
    

pessoa1 =Pessoa(27,"Ana","Rua 1")
print(pessoa1.getNome())
print(pessoa1.idade)
print(pessoa1.endereco)


pessoa1.setIdade(28)
print(pessoa1.idade)
