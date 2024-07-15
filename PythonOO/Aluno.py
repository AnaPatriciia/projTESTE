class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        #self.notas = [nota1,nota2,nota3,nota4] MAIS UMA OPÇÃO
        self.nota1 =nota1
        self.nota2 =nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def mostrarSituacão(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

        if media <5:
            return "Reprovado"
        elif media >=5 and media<=6.9:
            return "Exame"
        else:
            return "Aprovado"

aluno1 = Aluno("Wendril",1122,7.8,8.5,8.9,9.5)

print(aluno1.nome, aluno1.mostrarSituacão())


    
