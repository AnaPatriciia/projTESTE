class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def depositar(self, valor):   # Método para depositar dinheiro
        if valor > 0:
            self.saldo += valor
            print(f"Depositado: R${valor:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor): # Método para sacar dinheiro
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Sacado: R${valor:.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def imprimir_saldo(self):  # Método para imprimir o saldo
        print(f"Saldo atual: R${self.saldo:.2f}")

conta = Conta(12345, "João", 500)

conta.depositar(150)

conta.sacar(100)

conta.imprimir_saldo()

