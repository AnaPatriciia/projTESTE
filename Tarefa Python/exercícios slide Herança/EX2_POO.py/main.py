from Aluno import Aluno
from Professor import Professor

melhorprof = Professor(123,"THIAGO ALMEIDA",32,"Analista de Sistema / Filósofo de Boteco","TODAS",200,25000)

melhorprof.getDados()
print(melhorprof.lecionar())


estudante= Aluno(matricula=1231, nome="Ana", idade=20, notas=[9,8,7,6])
print(estudante.estudar())
print(f"Média do {estudante.nome}: {estudante.media:.2f}")


