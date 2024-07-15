#exercicio 4
def verificar_positivo_negativo(numero):
    if numero >0:
        return 'P'
    else:
        return 'N'
resultado1 =verificar_positivo_negativo(45)
resultado2 =verificar_positivo_negativo(-5)
resultado3 =verificar_positivo_negativo(0)
print(resultado1)
print(resultado2)
print(resultado3)