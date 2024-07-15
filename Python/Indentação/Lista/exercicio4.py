n1= float(input("Digite um número: "))
n2= float(input("Digite um número: "))
n3= float(input("Digite um número: "))
if(n1<n2<n3):
    print(f"A ordem é {n1},{n2} e {n3} ")
elif(n1<=n3<=n2):
    print(f"A ordem é {n1},{n3} e {n2}")
elif(n2<=n3<=n1):
    print(f" A ordem é {n2},{n3} e{n1}")
elif(n2<=n1<=n3):
    print(f"A ordem é {n2},{n1} e {n3}")
elif(n3<=n2<=n1):
    print(f"A ordem é {n3},{n2} e {n1}")
elif(n3<=n1<=n2):
    print(f"A ordem é {n3},{n1} e {n2}")
else:
    print("Não esta na ordem!")

