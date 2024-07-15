from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
    
    def apresentar_documento(self):
        print(f"{self.nome} apresenta o CNPJ: {self.cnpj}.")
