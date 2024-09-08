# Programa que peça dois números e imprima o maior deles.

mensagem = "quem é maior?"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

numero_1 = int(input("Digite um número:  "))
numero_2 = int(input("Digite outro número:  "))

if numero_1 > numero_2:
    print(f"\nO número {numero_1} é maior que o número {numero_2}")
elif numero_2 > numero_1:
    print(f"\nO número {numero_2} é maior que o número {numero_1}")
else:
    print("\nOs números são iguais")
