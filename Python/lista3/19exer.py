numero = int(input("Digite um número entre 100 e 9999: "))


if 100 <= numero <= 9999:
    temp = numero
    divisor = 10 ** (len(str(numero)) - 1)
   
    while divisor > 0:
        digito = temp // divisor
        print(digito)
        temp = temp % divisor
        divisor = divisor // 10
else:
    print("Número fora do intervalo permitido. Tente novamente.")