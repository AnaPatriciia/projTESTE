def calcular_consumo(distancia_km, litros_consumidos):
    consumo_km_por_litro = distancia_km / litros_consumidos

    if consumo_km_por_litro < 8:
        mensagem = "Gasta muito!"
    elif consumo_km_por_litro >= 8 and consumo_km_por_litro <= 15:
        mensagem = "Econômico!"
    else:
        mensagem = "Super econômico!"


    return consumo_km_por_litro, mensagem

distancia = 200  
litros = 20      

consumo, mensagem = calcular_consumo(distancia, litros)
print(f"Consumo: {consumo:.2f} Km/l - {mensagem}")


distancia = 400  
litros = 25      

consumo, mensagem = calcular_consumo(distancia, litros)
print(f"Consumo: {consumo:.2f} Km/l - {mensagem}")
