num = [7,3,45,99,36]
print(len(num))
num.append([2.5,1.9,9.7,7.5,3.8])

print(num)
num.pop()
num.pop()
print(num)
print(len(num))
lista = sorted(num)
print(lista)
print(max(num))
print(min(num))
lista.sort(reverse=True)
print(lista)
print("Media", sum(num) / len(num))
num.insert(0,9)
num.insert(1,8)




