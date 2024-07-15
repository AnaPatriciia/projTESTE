def tabela_precos():
    preco_item =1.99
    tab_precos ={}
    for quantidade in range (1,51):
        valor_total = quantidade * preco_item
        tab_precos [quantidade]= round (valor_total,2)
        return tab_precos
    
tabela = tabela_precos()
for quatidade, valor in tabela.items():
    print(f'{quatidade} intens : R$ {valor:.2f}')