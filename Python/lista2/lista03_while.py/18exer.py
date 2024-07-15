n = int(input("Quantos números: "))
num = []
cont = 0

while cont <n:
    num.append(float(input("Digite o Valor: ")))
    cont = cont + 1
print(max(num))