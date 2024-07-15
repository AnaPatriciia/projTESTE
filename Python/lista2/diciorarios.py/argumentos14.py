def calcula_valor(consumo,preco):
    valor = consumo * preco
    return valor

def calcula_consumo(potencia,horas,preco):
    consumo = potencia * horas / 1000
    conta= calcula_valor(consumo, preco)
    return conta

potencia = int(input("Digite a potencia do aparelho: "))
tempo = int(input("Quanto tempo foi utilizado no mês: "))
preco = float(input("Valor do KWh: "))

banho = calcula_consumo(potencia,tempo,preco)#parametros
print("R$: ",banho)