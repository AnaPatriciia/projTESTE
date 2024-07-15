from PassagemAviao import PassagemAviao
from PassagemBus import PassagemBus

# Passagem de Avião
aviao = PassagemAviao(500.0, "C3", "P1", True)
print(f"Preço: R${aviao.preco}, Assento: {aviao.assento}")

aviao.alterar_preco(550.0)   #Alterar prço
aviao.escolher_assento("A5")  #Alterar assento
print(f"Novo Preço: R${aviao.preco}\n Novo Assento: {aviao.assento}")

aviao.decolar()
aviao.realizar_checkin()


# Passagem de Ônibus
onibus = PassagemBus(100.0, "20", "ABC1234", True)
print(f"Preço: R${onibus.preco}, Assento: {onibus.assento}")

onibus.alterar_preco(110.0) #alterar preço
onibus.escolher_assento("10") #Alterar assento
print(f"Novo Preço: R${onibus.preco}, Novo Assento: {onibus.assento}")

onibus.embarcar()
onibus.ajustar_leito()

