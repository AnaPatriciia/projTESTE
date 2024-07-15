from Passagem import Passagem

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito
    
    def embarcar(self):
        print(f"Ônibus com placa {self.placa} embarcando.")
    
    def ajustar_leito(self):
        if self.leito:
            print("Modo leito ativado.")
        else:
            print("Modo leito desativado.")

   
