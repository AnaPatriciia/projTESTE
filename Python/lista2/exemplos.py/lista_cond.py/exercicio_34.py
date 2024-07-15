p=float(input("Digite o valor: "))
if(p<=50):
    np= p+(p * 0.05)
elif(p>50 and p<=100):
    np=p +(p * 0.10)
else:
    np= p + (p * 0.15)
    print(np)