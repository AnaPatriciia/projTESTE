#crie uma função que receba múltiplos argumentos não nomeados, considere que a função receba números interiros
#como argumentos e retorne a soma dos argumentos
def soma( *args):
    total =  sum(args)
    return total

numero = soma(1, 2, 3, 4, 5)
print(numero)




