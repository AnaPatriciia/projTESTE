i = float(input("Importâcia: "))
p = (i * 0.46)
g1 = i - p
s = (i * 0.32)
g2 = (i -s)
g3 = (g1 + g2) -i
print(f"O primeiro ganhador rescebera {g1} o segundo recebera {g2} e terceiro {g3}")
