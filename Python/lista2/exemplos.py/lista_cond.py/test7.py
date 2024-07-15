pa = float(input("Digite o valor de aquisição do produto: "))
if (pa < 50.00):
    
    pv = pa + (pa * 0.45)
    print(f"O preço de venda do produto é: R$ {pv:.2f}")
elif (pa >= 50.00):
    
    pv = pa + (pa * 0.30)
    print(f"O preço de venda do produto é: R$ {pv:.2f}")