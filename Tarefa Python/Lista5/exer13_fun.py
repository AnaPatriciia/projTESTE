# Elabore uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o
# resultado de XZ para o programa principal. Atenção não utilize nenhuma função pronta de
# exponenciação.
def calcula_potencia(X, Z):
   
    if Z == 0:
        return 1
  
    elif Z < 0:
        X = 1 / X
        Z = -Z

    resultado = 1 
    contador = 0   
    while contador < Z: 
        resultado =resultado * X  
        contador += 1 
    
    return resultado


X = 2
Z = 3

resultado = calcula_potencia(X, Z)
print(f"O resultado de {X} elevado a {Z} é: {resultado}")
