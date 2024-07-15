
def verificar_numero(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

numero = float(input("Digite um número: "))

resultado = verificar_numero(numero)
print(f"O resultado é: {resultado}")
