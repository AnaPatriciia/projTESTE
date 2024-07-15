h=float(input("Horas trabalhadas: "))
vh=40.50
ht=(h*vh)
if(ht>2500.00):
    t=(2500.00**0.11)
    print(f"Salário: {t}")
elif( ht<2500.00):
    print(f"Salário: {ht}")

