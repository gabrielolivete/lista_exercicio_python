# Programa para calcular a quantidade de tinta a ser utilizada para pintar uma parede e o valor total da compra
import math

mensagem = "decor tintas orçamento"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

area_parede = float(input("Digite a área de parede a ser pintada:  "))
tinta = (area_parede / 6) * 1.1

lata = 18
qtd_lata = tinta / lata
lata_valor = 80
custo_lata = math.ceil(qtd_lata) * lata_valor

galao = 3.6
qtd_galao = tinta / galao
galao_valor = 25
custo_galao = math.ceil(qtd_galao) * galao_valor

mix_lata = 0
mix_galao = 0
resto = tinta % lata

if (qtd_galao >= 3) and (resto / galao <= 3):
    mix_lata = math.floor(tinta / lata)
    mix_galao = math.ceil((tinta - round(mix_lata * 18)) / galao)
elif (qtd_galao >= 3) and (resto / galao > 3): 
    mix_lata = math.ceil(tinta / lata)
else:
    mix_galao = math.ceil((tinta - round(mix_lata * 18)) / galao)

print(f"""\nORÇAMENTOS DISPONÍVEIS\n
    
    Quantidade necessária de tinta: {math.ceil(tinta)}L

    1. Somente latas de 18L:
        - Necessidade de {math.ceil(qtd_lata)} lata(s).
        CUSTO: R${custo_lata:.2f}

    2. Somente galões de 3,6L:
        - Necessidade de {math.ceil(qtd_galao)} galão(ões).
        CUSTO: R${custo_galao:.2f}

    3. Mesclar embalagens:
        - Lata: {mix_lata} lata(s)
        - Galão: {mix_galao} galão(ões)
        CUSTO: R${((mix_lata * lata_valor) + (mix_galao * galao_valor)):.2f}""")
