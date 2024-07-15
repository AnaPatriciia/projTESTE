class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def setAlterarPreco(self,novo_Preco):
        self.preco = novo_Preco

    def getMostrarSetor(self):
        return self.setor