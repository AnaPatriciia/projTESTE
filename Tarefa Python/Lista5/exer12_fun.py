def soma_numeros_entre(num1, num2):
    if num1 > 0 and num2 > 0:
        menor = min(num1, num2)
        maior = max(num1, num2)
        soma = 0
        for i in range(menor + 1, maior):
            soma += i
        return soma
    else:
        return "Digite números inteiros positivos."

num1 = 3
num2 = 7

resultado = soma_numeros_entre(num1, num2)
print("A soma dos números entre", num1, "e", num2, "é:", resultado)
