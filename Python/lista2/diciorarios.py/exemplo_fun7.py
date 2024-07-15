
def calcular_salario(horas_trabalhadas, salario_por_hora):
    carga_horaria_base = 40
    taxa_horas_extras = 1.5

    if horas_trabalhadas <= carga_horaria_base:
        salario = horas_trabalhadas * salario_por_hora
    else:
        horas_extras = horas_trabalhadas - carga_horaria_base
        salario_base = carga_horaria_base * salario_por_hora
        salario_horas_extras = horas_extras * salario_por_hora * taxa_horas_extras
        salario = salario_base + salario_horas_extras
    return salario

horas_trabalhadas = 45
salario_por_hora = 20
salario_total = calcular_salario(horas_trabalhadas, salario_por_hora)
print(f'O salario total para {horas_trabalhadas} horas trabalhadas é R$ {salario_total}')
