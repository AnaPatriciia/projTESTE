def reverso_numero(numero):
    reverso = 0
    while numero > 0:
        digito = numero % 10  
        reverso = reverso * 10 + digito  
        numero = numero // 10  
    return reverso

numero = int(input("Digite um número inteiro para obter o seu reverso: "))
reverso = reverso_numero(numero)
print(f"O reverso de {numero} é: {reverso}")
