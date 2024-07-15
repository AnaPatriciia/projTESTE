h= float(input("Altura: "))
s= input("Sexo femenino(F), masculino(M): ")
m=(72.7*h)-58
f=(62*h)-44,7
if(s=="M"):
    print("O peso ideal é",m)
elif(s=="F"):
    print("O peso ideal é",f)