numeros = [2,3,4,11,5,9,12,97,24]
i = 0 
#Parando/ encerando o loop, se 11 for encontrado
while i< len(numeros):
    print(numeros[i])
    if numeros[i] == 11:
        print('Encontramos o número 11!')
        break
    else:
        i = i + 1