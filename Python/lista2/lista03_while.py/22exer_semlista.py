soma = 0
cont = 0

while True:
    nota = int(input("NOTA: "))
    if nota < 0 or nota > 10:
        break
    else:
        soma += nota
        cont=cont+1

print("Media", soma / cont)
