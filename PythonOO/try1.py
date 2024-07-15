#try2
i = 0
soma = 0
while i < 10:
    try:
        x = int(input("Digite um número: "))
        soma += x
        i +=1
    except:
        print("Valor invalido! tente novamente!")

print(soma)