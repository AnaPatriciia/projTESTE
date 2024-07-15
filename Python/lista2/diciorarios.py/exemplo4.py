#exercicio 8
estoque={
    "calça":"5",
    "blusa":"10",
    "camisa":"8",
}
for i in estoque.keys():
    produto=input("Digite o produto: ")
    if produto in estoque.keys():
        print(f"O estoque de {produto} é de {estoque[produto]} unidades.")
    else:
        print(f"{produto} não tem em estoque.")