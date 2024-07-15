def calcular_volume_esfera(raio):
    volume = (4/3) * 3.14 * raio**3
    return volume

raio = float(input("Digite o raio da esfera: "))
volume = calcular_volume_esfera(raio)
print(f"O volume da esfera com raio {raio} é: {volume:.2f} unidades cúbicas.")
