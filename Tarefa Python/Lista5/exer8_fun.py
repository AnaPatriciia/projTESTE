def celsius_para_fahrenheit(temp_celsius):
    temp_fahrenheit = temp_celsius * (9.0/5.0) + 32.0
    return temp_fahrenheit

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"A temperatura de {temperatura_celsius:.1f} graus Celsius equivale a {temperatura_fahrenheit:.1f} graus Fahrenheit.")
