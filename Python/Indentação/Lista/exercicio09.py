n = float(input("Digite um número: "))
if( n > 0) and (n ** 0.5 == 0.0):
    r = (n ** 0.5)
    print(f"A raiz quadrada de {n} é {r}.")
elif (n < 0 )or (n ** 0.5 != 0.0):
    print("Número inválido.")
else:
    print("O número digitado é zero.")