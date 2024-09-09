# Programa que pergunte o preço de dois ou mais produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

mensagem = "economizando na compra"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

lista_dicionario = []

numero_registros = int(input("Digite quantos produtos deseja comparar:  "))

for i in range(numero_registros):
    produto = {}
    produto['nome'] = input(f"Digite o nome do produto {i + 1}:  ")
    produto['valor'] = float(input(f"Digite o valor do produto {i + 1}:  "))
    lista_dicionario.append(produto)

lista_ordenada = sorted(lista_dicionario, key=lambda x: x['valor'])

item_barato = lista_ordenada[0]

print(f"{item_barato['nome']} a R${item_barato['valor']} é o item mais barato")
