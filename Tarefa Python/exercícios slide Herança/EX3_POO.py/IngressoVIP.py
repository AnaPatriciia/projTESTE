from Ingresso import Ingresso
class IngressoVIP(Ingresso):
    def __init__(self, preco, setor,camarote,open_bar,open_food,estacionamento):
        super().__init__(preco, setor)
        self.camarote =camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            return "Pegar bebida"
        
        else: 
            return "Este não é um ingresso VIP"
        
    def acessar_camarote(self):
        if self.camarote:
            return "Acesso ao camarote"
        
        else:
            "Acesso negado"