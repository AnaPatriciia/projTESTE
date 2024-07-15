def calculo_media( *args):
    if not args:
        return 0
    soma = sum(args)
    quantidade = len(args)
    media = soma /quantidade
    return media
resultado = calculo_media(1.2,3.4,5.6)
print(f"A média dos resultados é {resultado}")
print(type(resultado))




    