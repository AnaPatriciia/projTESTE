import random

def embaralha_string(s):
    lista_caracteres = list(s)

    random.shuffle(lista_caracteres)    # random.shuffle é usado para embaralhar os elementos de uma lista de forma aleatória

    
    string_embaralhada = ''.join(lista_caracteres)

    return string_embaralhada


s = "Python"
resultado = embaralha_string(s)
print(f"A string embaralhada é: {resultado}")
