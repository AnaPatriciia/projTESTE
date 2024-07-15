def calcula_operacao(valor1, valor2, operacao):
    if operacao == '+':
        resultado = valor1 + valor2
    elif operacao == '-':
        resultado = valor1 - valor2
    elif operacao == '*':
        resultado = valor1 * valor2
    elif operacao == '/':
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            return "Divisão por zero não é permitida."
    else:
        return "Operação inválida."

    return resultado

valor1 = 10
valor2 = 5

resultado_adicao = calcula_operacao(valor1, valor2, '+')
resultado_subtracao = calcula_operacao(valor1, valor2, '-')
resultado_multiplicacao = calcula_operacao(valor1, valor2, '*')
resultado_divisao = calcula_operacao(valor1, valor2, '/')

print("Adição:", resultado_adicao)
print("Subtração:", resultado_subtracao)
print("Multiplicação:", resultado_multiplicacao)
print("Divisão:", resultado_divisao)
