c= input("Cargo desejado: ")
n= input("Nome completo:")
i=int(input("Idade: "))
e=input("email: ")

if(i>=18):
    print("Parabens você passou para fase 1.")
    curso =input("Você possui curso na áera: ")
    if(c=="Sim"):
        print("Parabéns você passou para fase 2")
        n=float(input("Digite sua nota: "))
        if(n>=7):
            print("Parabens você para fase final")
        else:
            print("Parabens você passou para fase final")
    else:
        print("Obrigado pela participação")
else:
    print("Obrigado pela participação.")