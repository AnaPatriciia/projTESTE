class Professor:
    def __init__(self,matricula,nome,cpf,idade): #Método construtor
         self.matricula = matricula #Atributo
         self.nome = nome  #Atributo
         self.cpf = cpf #Atributo
         self.idade = idade #Atributo

    def hello(self): #Métodos
         print(f"Olá Professor {self.nome}")

    def mostrarDados(self):
         print(f"Matricula: {self.matricula}")
         print(f"Nome: {self.nome}")
         print(f"CPF: {self.cpf}")
         print(f"Idade: {self.idade}")

prof =Professor("123","Thiago","654321","20")
prof.hello()