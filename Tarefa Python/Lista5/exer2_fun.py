def data(dia, mes, ano):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }

    mes_extenso = meses.get(mes, "Mês inválido")
    if mes_extenso == "Mês inválido":
        return mes_extenso

    return f"{dia} de {mes_extenso} de {ano}"

dia = 1
mes = 1
ano = 2000
print(data(dia, mes, ano))
