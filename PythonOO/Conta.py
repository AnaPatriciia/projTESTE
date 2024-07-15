class Conta:
    def __init__(self,nome,cpf,numero,saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def getNome(self):
        return self.nome
    
    def getCpf(self):
        return self.cpf
    
    def getNumero(self):
        return self.numero
    
    def getSaldo(self):
        return self.saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito no valor de R${valor:.2f}.")
        else:
            print("Valor de depósito inválido.")

   
    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque no valor de R${valor:.2f} realizado.")
        elif valor > 0 and self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido.")

   
    def imprimir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
conta = Conta("Ana", "123.456.789-00", "1234567")
conta.imprimir_saldo()
conta.depositar(1000)
conta.imprimir_saldo()
conta.sacar(300)
conta.imprimir_saldo()
conta.sacar(800)
conta.imprimir_saldo()
conta.sacar(200)
conta.imprimir_saldo()