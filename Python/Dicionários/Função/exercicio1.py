def pot(base,n):
    for i in range(1,n+1):
        res = base **i
        print(f"{base}** {i}={res}")
    
base= int(input("Digite um numero: "))
n= int(input("Digite um número: "))


pot(base,n)
    
