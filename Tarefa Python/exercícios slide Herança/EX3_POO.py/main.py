from IngressoVIP import IngressoVIP
from Ingresso import Ingresso

ingresso1= Ingresso(50,"VIP") #exibir o preço inicial
print("Preço: ",ingresso1.preco)

ingresso1.setAlterarPreco(100) #alterar o preço
print("Preço do ingresso VIP:", ingresso1.preco) 

#Ingresso vip
ingresso_vip = IngressoVIP(preco=100, setor='VIP', camarote=True, open_bar=True, open_food=False, estacionamento=True)

print("Setor do ingresso:", ingresso_vip.getMostrarSetor()) 
print("Open bar:", ingresso_vip.pegar_bebida())            
print("Camarote:", ingresso_vip.acessar_camarote())  

