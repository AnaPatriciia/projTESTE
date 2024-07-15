class Funcionario:
    def __init__(self,nome,sobrenome,horas_trabalhadas,valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = float(horas_trabalhadas)
        self.valor_hora = float(valor_hora)


    def getNomeCompleto(self):
        return self.nome + " " + self.sobrenome
    
    def getcalcularSalario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        return salario
    
    def incrementarHoras(self,valorPorHora):
        self.valor_hora += float(valorPorHora)
    

dados = Funcionario("Ana", "Oliveira","123","40") 

print("Nome:", dados.getNomeCompleto())   #exibe o nome completo

total = dados.getcalcularSalario()   #mostra valor do salario
print("Total por horas trabalhadas: ",dados.getcalcularSalario())

dados.incrementarHoras(10)   #incrementar horas trabalhadas
novoToal= dados.getcalcularSalario()
print("Total de horas trabalhadas atualizado: ",dados.getcalcularSalario())





