soma = 0
contador = 0
for num in range (0,200):
    if num % 2 == 0:
        soma += num
        contador += 1
        if contador ==50:
            break
print(f"A soma dos 50 primeiros numeros pares é: {soma}")