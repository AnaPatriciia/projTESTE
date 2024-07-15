n1= float(input("Nota 1: "))
n2= float(input("Nota 2: "))
n3= float(input("Nota 3: "))
media = (((n1 *1) + (n2 * 1) + (n3 * 2)) /4) * 10
print(media)
if(media>=70):
    print("Aprovado")
elif(media<70 and media>=30):
    print("Recuperação!!")
else:
    print("Reprovado")