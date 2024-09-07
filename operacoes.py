# Programa que peça dois números inteiros e um número real, calcule e mostre:
# o produto do dobro do primeiro com metade do segundo
# a soma do triplo do primeiro com o terceiro
# o terceiro elevado ao cubo

mensagem = "operações com inteiros e reais"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

nint_1 = int(input("Digite um número inteiro:  "))
nint_2 = int(input("Digite outro número inteiro:  "))
nreal = float(input("Digite um número real qualquer:  "))

solucao_1 = (nint_1 * 2) * (nint_2 / 2)
solucao_2 = (nint_1 * 3) + nreal
solucao_3 = nreal**3

print(f"\nSolução 1:\nO produto entre o dobro de {nint_1} e a metade de {nint_2} é igual a {solucao_1}")
print(f"\nSolução 2:\nA soma entre o triplo de {nint_1} e {nreal} é igual a {solucao_2}")
print(f"\nSolução 3:\nO valor de {nreal} elevado ao cubo é igual a {solucao_3:.2f}")
