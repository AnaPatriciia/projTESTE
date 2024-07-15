#exercicio 5
amigos ={
    "amigo1":{"nome": "João","idade":"20"},
    "amigo2":{"nome": "Pedro","idade":"20"},
    "amigo3":{"nome" : "Jean", "idade":"21"}
}
for nome, idade in amigos.items():
    print(f"{nome} tem {idade} anos.")

#exercicio 6
nome_amigos= input("Digite o nome do amigo: ")
if nome_amigos in amigos:
    print(f"{nome_amigos} esta na lista ")
else: 
    print(f"{nome_amigos} não esta na lista")