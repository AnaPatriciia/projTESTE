#exercicio 7

dicionario={
    "yes": "sí",
     "hello": "hola",
    "goodbye": "adios",
}
palavra=input('Digite a palavra: ')
if palavra in dicionario.keys():
    print(f" {dicionario[palavra]}")
else:
    print(" Não encontrada no dicionário. ")