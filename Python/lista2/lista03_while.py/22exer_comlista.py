
notas = []
cont = 0

while True:
    nota = int(input("Quantidade de notas: "))
    if nota < 0 or nota > 10:
        break
    else:
        notas.append(nota)
        cont=cont+1

print("Media", sum(notas) / len(notas))
