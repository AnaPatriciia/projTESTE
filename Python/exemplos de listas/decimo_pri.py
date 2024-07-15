numeros= [2,11,4,11,5,9,99,11]
i = -1
contador = 0
print(len(numeros))
while i <len(numeros) -1:
    i = i + 1
    if numeros [i] != 11:
        continue
else:
    print("11 esta aqui!")
    contador +=1
print("Quantidade de numeros 11 encontrados: ",contador)