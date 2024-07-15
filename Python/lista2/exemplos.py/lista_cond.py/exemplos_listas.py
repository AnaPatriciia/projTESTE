numeros = [24,12,33,99,7,8.18,10.5,54]
#somar numeros dentro da lista
print(numeros[3]+numeros[4])
#achar o menor numero da lista 
print(min(numeros))
#maior numero da lista
print(max(numeros))
#a soma de todos os numeros da lista
print(sum(numeros))
#ordem crescente
lista_ordenada = sorted(numeros)
print(lista_ordenada)
#a media dos numeros da lista
print("Media", sum(numeros) / len(numeros))
#posição do numero
indice = numeros.index(8.18)
print(indice)
#tirar o ultimo numero
numeros.pop()
numeros.pop()
print(numeros)
print(len(numeros))
#inserir um numero na lista
numeros.insert(0,"Ana")
numeros.insert(2,1996)
print(numeros)
#numeros.append(51)
#numeros.append("Segundona ")
#print(numeros)

numeros.append([1,2,3,4])
print(numeros[8])