venda= float(input("Digite o valor da casa: "))
if(venda>=100000):
    com= (venda * 16 /100) + 700
    print(com)
elif(venda<100000 and venda>=800000):
    com=(venda *14 / 100) +650
elif(venda<80000 and venda>=60000):
    com=(venda *14 / 100)+ 600
elif(venda<60000 and venda>=40000):
    com=(venda *14 / 100) +550
elif(venda<40000 and venda>=20000):
    com=(venda *14 / 100) +500
    print(com)
else:
    com=(venda *14 /100)
    print(com)
