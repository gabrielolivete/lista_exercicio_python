# Programa que peça um número e então mostre a mensagem "O número informado foi [número]."

mensagem = "identificador de números inteiros"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

numero_informado = int(input("Digite qualquer número inteiro:  "))

print(f"\nO número informado foi {numero_informado}")
