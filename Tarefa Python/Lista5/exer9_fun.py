def calcular_volume_cilindro(raio, altura):
    volume = 3.14 * raio**2 * altura
    return volume

# Programa de teste
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))
volume = calcular_volume_cilindro(raio, altura)
print(f"O volume do cilindro com raio {raio} e altura {altura} é: {volume:.2f} unidades cúbicas.")
