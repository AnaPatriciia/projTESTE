s=int(input("Salário: "))
p=int(input("Prestação: "))
l= (s**0.02)
if(p>l):
    print("Emprestimo não concedido!")
else:
    print("Emprestimo concedido!")