v = int(input("Valores: "))
valor = []
cont = 0

while cont <v:
    valor.append(float(input("Digite o Valor: ")))
    cont = cont + 1
print(sum(valor))