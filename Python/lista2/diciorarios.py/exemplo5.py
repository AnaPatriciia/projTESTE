
texto= input("Insira o texto: ")
palavras= texto.split()
cont_palavras ={} 
for palavra in palavras:
    if palavra in cont_palavras:
        cont_palavras[palavra]+=1
    else:
        cont_palavras[palavra]= 1
print(cont_palavras)
