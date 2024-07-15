lista=[1,2,-3,4,5,6,7,8,9,-10]
for item in lista:
    if item =="-1":
        continue
print(item)
print("Media", sum(lista) / len(lista))
