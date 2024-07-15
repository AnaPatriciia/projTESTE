class Aluno2:
    def __init__(self,nome,ra,notas):
        self.nome = nome
        self.ra = ra
        self.notas = notas
        

    def mostrarSituacão(self):
        media = sum(self.notas) / len(self.notas)

        if media <5:
            return "Reprovado"
        elif media >=5 and media<=6.9:
            return "Exame"
        else:
            return "Aprovado"

notas = []
nome =input("Nome do aluno: ")
ra = int(input("Digite o ra do aluno: "))

i = 0
while i <4:
    nota= float("Digite a nota do aluno: ")
    notas.append(notas)
    i = i + 1

a = Aluno2(nome,ra,notas)
print(a.mostrarSituacão())

    
