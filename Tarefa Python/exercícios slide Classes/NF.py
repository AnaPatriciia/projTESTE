class NF:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi

    def getNumero(self):
        return self.numero

    def getDataEmissao(self):
        return self.data

    def setRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social

    def calcularValorTotal(self):
        valor_total = self.valor_produtos + self.frete + self.icms + self.ipi
        return valor_total


numero = input("Número da Nota Fiscal: ")
tipo = input("Tipo da Nota Fiscal: ")
serie = int(input("Série da Nota Fiscal (1, 2 ou 3): "))
cnpj = input("CNPJ: ")
razao_social = input("Razão social: ")
data = input("Data de emissão (dd/mm/yyyy): ")
valor_produtos = float(input("Valor dos produtos: "))
icms = float(input("Valor do ICMS: "))
frete = float(input("Valor do frete: "))
ipi = float(input("Valor do IPI: "))

nota_fiscal = NF(numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi)


numero_nota = nota_fiscal.getNumero()
print(f"Número da Nota Fiscal: {numero_nota}")


data_emissao = nota_fiscal.getDataEmissao()
print(f"Data de Emissão: {data_emissao}")

nova_razao_social = input("Digite a nova razão social: ")
nota_fiscal.setRazaoSocial(nova_razao_social)
print(f"Razão Social alterada para: {nota_fiscal.razao_social}")

valor_total = nota_fiscal.calcularValorTotal()
print(f"Valor Total da Nota Fiscal: R$ {valor_total:.2f}")

