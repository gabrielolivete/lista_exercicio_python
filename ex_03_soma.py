# Programa que peça dois números e imprima a soma.

mensagem = "a grande soma"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

numero_1 = float(input("Digite o primeiro número:  "))
numero_2 = float(input("\nDigite o segundo número:  "))

soma = numero_1 + numero_2

print(f"\nA soma entre {numero_1} e {numero_2} é {soma}")
