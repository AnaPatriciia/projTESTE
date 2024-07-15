class Pessoa:
    def __init__(self,nome,idade,endereco): # Método construtor
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def getNome(self):   #Método 
        return self.nome

    def setIdade(self,nova_idade): #Médodo que vai ser usado para alterar idade
        self.idade = nova_idade

    def imprimir_endereco(self):  # Método para imprimir o endereço
        return f"Endereço: {self.endereco}"
        
cadastro = Pessoa("Ana","27","Rua A") 
print("Nome",cadastro.getNome()) #Mostrar nome

print("Idade",cadastro.idade)

print("Endereço: ",cadastro.endereco)  #Imprimir endereço

cadastro.setIdade(28) # Alterar a idade
print("Idade atualizada: ", cadastro.idade)

