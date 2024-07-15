
def financiamento():
   
    valor_veiculo = float(input("Digite o valor do veículo: R$ "))
    valor_entrada = float(input("Digite o valor da entrada: R$ "))
    taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100
    num_parcelas = int(input("Digite o número de parcelas: "))

    valor_financiado = valor_veiculo - valor_entrada

    valor_parcela = valor_financiado * ((taxa_juros * (1 + taxa_juros)**num_parcelas) / ((1 + taxa_juros)**num_parcelas - 1))

 
    valor_total_pago = valor_parcela * num_parcelas
    juros_pagos = valor_total_pago - valor_financiado

   
    print("\n--- Detalhes do Financiamento ---")
    print(f"Valor do veículo: R$ {valor_veiculo:.2f}")
    print(f"Valor da entrada: R$ {valor_entrada:.2f}")
    print(f"Valor financiado: R$ {valor_financiado:.2f}")
    print(f"Taxa de juros: {taxa_juros * 100:.2f}% ao mês")
    print(f"Número de parcelas: {num_parcelas}")
    print(f"Valor da parcela: R$ {valor_parcela:.2f}")
    print(f"Valor total pago: R$ {valor_total_pago:.2f}")
    print(f"Juros pagos: R$ {juros_pagos:.2f}")


financiamento()