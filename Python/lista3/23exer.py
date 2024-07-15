num =int(input("Digite um número: "))
divisiveis=[]
i = num
while i > 0:
    if i == num:
        i = i - 1
    elif num  % i == 0:
        divisiveis.append(i)
        i = i - 1
    else:
        i = i - 1
print(divisiveis)
print(sum(divisiveis))