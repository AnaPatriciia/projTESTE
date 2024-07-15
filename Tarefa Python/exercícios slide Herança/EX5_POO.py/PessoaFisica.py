from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
    
    def apresentar_documento(self):
        print(f"{self.nome} apresenta o CPF: {self.cpf}.")
