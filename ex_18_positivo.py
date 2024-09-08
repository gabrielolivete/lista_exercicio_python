# Programa que peça um valor e mostre na tela se o valor é negativo ou positivo

mensagem = "positivo ou negativo?"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

valor = int(input("Digite um valor inteiro qualquer: "))

if valor < 0:
    print(f"\n{valor} é negativo")
elif valor > 0:
    print(f"\n{valor} é positivo")
elif valor == 0:
    print(f"\n{valor} é nulo")
