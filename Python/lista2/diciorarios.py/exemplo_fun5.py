def somaimposto(taxaimposto,custo):
    taxa_decimal = taxaimposto /100
    novo_custo = custo + (custo * taxa_decimal)
    return novo_custo

taxa= 10
custo_inicial= 100
custo_final= somaimposto(taxa, custo_inicial)
print(f"Com uma taxa de imposto {taxa}%, 0 custo final é: R$ {custo_final}")