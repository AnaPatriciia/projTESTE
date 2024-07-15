from Passagem import Passagem

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portao_embarque, checkin):
        super().__init__(preco, assento)
        self.portao_embarque = portao_embarque
        self.checkin = checkin
    
    def decolar(self):
        print(f"Avião decolando do portão {self.portao_embarque}.")
    
    def realizar_checkin(self):
        if self.checkin:
            print("Checkin realizado com sucesso.")
        else:
            print("Não é possível realizar o checkin.")

