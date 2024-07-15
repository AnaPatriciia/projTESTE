def calcula_media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)
    return media

lista_de_numeros =[8,9,20,22,55,3,6,7,10,11]
x =calcula_media(lista_de_numeros)
print(x)

#outro exemplo do mesmo exercicio
#def calcula_media(lista):
#   media = sum(lista) / len(lista)
#    return media

#lista_de_numeros =[8,9,20,22,55,3,6,7,10,11]
#x =calcula_media(lista_de_numeros)
#print(x)