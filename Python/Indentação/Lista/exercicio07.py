pa = float(input("Digite o preço de aquisição do produto: R$ "))

if pa < 50.00:
    pv = (pa * 1.45)  
else:
    pv = (pa * 1.3)  

print("O preço de venda do produto será: R$ ",pv)