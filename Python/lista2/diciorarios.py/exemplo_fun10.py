def calcularTempo(tempo_minutos):
    
    tarifa_minima = 9.00
    tarifa_adicional = 1.50
    tempo_corte_gratuito = 15
   
    pis = 0.0033
    cofins = 0.0020
    icms = 0.17

  
    tempo_horas = tempo_minutos / 60
   
    
    if tempo_minutos < tempo_corte_gratuito:
        valor_sem_impostos = 0.0
    elif tempo_horas <= 1:
        valor_sem_impostos = tarifa_minima
    else:
        valor_sem_impostos = tarifa_minima + (tempo_horas - 1) * tarifa_adicional
   
    valor_pis = valor_sem_impostos * pis
    valor_cofins = valor_sem_impostos * cofins
    valor_icms = valor_sem_impostos * icms
   
   
    total_impostos = valor_pis + valor_cofins + valor_icms
   
    
    valor_total = valor_sem_impostos + total_impostos
   
   
    print(f"Tempo {tempo_horas:.1f} horas")
    print(f"PIS R$ {valor_pis:.2f}")
    print(f"COFINS R$ {valor_cofins:.2f}")
    print(f"ICMS R$ {valor_icms:.2f}")
    print(f"IMPOSTOS R$ {total_impostos:.2f}")
    print(f"TOTAL R$ {valor_total:.2f}")


tempo_utilizado = 240 
calcularTempo(tempo_utilizado)

