#n = int(input("Digite o num de avaliações: "))
#i = 0
#soma= 0
#while i < n:
#    soma += int("Digite sua nota: ")
#    i += 1
#media = soma/n
#print(media)

numero_notas = int(input("Digite o numero de notas:"))
contador =0
notas=[]
while contador < numero_notas:
    notas.append(int(input("Digite a nota: ")))
    contador = contador +1
media = sum(notas) / len(numero_notas)
print(media)


