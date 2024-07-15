def dados_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} is {valor}")

def coletar_dados():
   
    firstname = input("Digite o primeiro nome: ")
    lastname = input("Digite o sobrenome: ")
    email = input("Digite o email: ")
    country = input("Digite o país: ")
    age = input("Digite a idade: ")
    phone = input("Digite o telefone: ")

    dados_pessoa(
        firstname=firstname,
        lastname=lastname,
        email=email,
        country=country,
        age=age,
        phone=phone
    )

coletar_dados()
    

  


