class Agenda:
    def __init__(self, dia, mes, ano, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def anotarTarefa(self, novaAnotacao):
        self.anotacao = novaAnotacao

    def mostrarAnotacao(self):
        if self.anotacao:
            return f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotacao}"
        else:
            return f"Sem anotação."

# Faltou o metodo validar data##

evento = Agenda("05", "07", "2024")
evento.anotarTarefa("SEXTOU!!!")
print(evento.mostrarAnotacao())


