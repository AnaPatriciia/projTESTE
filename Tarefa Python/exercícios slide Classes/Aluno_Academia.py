class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcularIMC(self):
        altura_metros = self.altura / 100  
        imc = self.peso / (altura_metros ** 2)
        return imc

    def obterValor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.9  #essa multiplicação é equivalente a um desconto de 10%
        else:
            return self.mensalidade


nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

aluno = Aluno_Academia(nome, idade, peso, altura)

imc_aluno = aluno.Calcular_IMC()
print(f"O IMC do aluno {aluno.nome} é: {imc_aluno:.2f}")

mensalidade_aluno = aluno.Obter_valor_mensalidade()
print(f"A mensalidade do aluno {aluno.nome} é: R$ {mensalidade_aluno:.2f}")
