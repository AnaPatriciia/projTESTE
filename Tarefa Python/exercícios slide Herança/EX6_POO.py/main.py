from Vendedor import Vendedor
from Gerente import Gerente

# Vendedor
vendedor = Vendedor("Ana", "12345", 3000.0, 500.0)
print(f"Nome: {vendedor.nome}\nMatrícula: {vendedor.matricula}\nSalário: R${vendedor.salario}\nComissão: R${vendedor.comissao}")

print(f"Salário total do vendedor {vendedor.nome}: R${vendedor.calcular_salario()}")   # salário do vendedor

if vendedor.bater_meta():     # Verificando se o vendedor bateu a meta
    print(f"{vendedor.nome} bateu a meta de vendas!")
else:
    print(f"{vendedor.nome} não bateu a meta de vendas.")

print("---"*9)

#Gerente
gerente = Gerente("Patrícia", "67890", 5000.0, "senha123")
print(f"Nome: {gerente.nome}\nMatrícula: {gerente.matricula}\nSalário: R${gerente.salario}\nSenha: {gerente.senha}")

print(f"Salário total do gerente {gerente.nome}: R${gerente.calcular_salario()}") #  salário do gerente

# Aprovando folga do gerente
print(gerente.aprovar_folga())
