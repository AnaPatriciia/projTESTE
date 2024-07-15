def calcula_media(nota1, nota2, nota3, opcao):
    if opcao == 'A':
        media_aritmetica = (nota1 + nota2 + nota3) / 3
        return media_aritmetica
    elif opcao == 'P':
        media_ponderada = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
        return media_ponderada
    else:
        return "Opção inválida. Use."


nota1 = 8
nota2 = 7
nota3 = 9

media_aritmetica = calcula_media(nota1, nota2, nota3, 'A')
media_ponderada = calcula_media(nota1, nota2, nota3, 'P')

print("Média Aritmética:", media_aritmetica)
print("Média Ponderada:", media_ponderada)

