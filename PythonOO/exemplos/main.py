from Estudante import Estudante
from Professor import Professor

matricula = input("Matircula: ")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
nota = input("Nota: ")

aluno1= Estudante(matricula,nome,idade,nota)

aluno1.mostrarDados() #Corrigir