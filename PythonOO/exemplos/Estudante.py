class Estudante:
    def __init__(self,matricula,nome,idade,nota):  # Método construtor
        self.matricula = matricula #Atributo
        self.nome = nome  #Atributo
        self.idade = idade #Atributo
        self.nota =nota  #Atributo

    def hello(self): #Métodos
            print(f"Olá {self.nome}")

    def mostrarDados(self): #métodos
         print(f" Matricula: {self.matricula}")
         print(f"Nome: {self.nome}")
         print(f"Idade: {self.idade}")
         print(f"Nota: {self.nota}")


aluno = Estudante(1212, "Pedro",18,80)
print(aluno.nome)
aluno2 = Estudante(1212, "Domitila",22,90)

print(aluno2.nome)
aluno2.hello()
aluno2.nome ="Ana Patrícia"
aluno2.mostrarDaodos()