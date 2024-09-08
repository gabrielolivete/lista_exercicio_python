# Programa que peça 4 notas e imprima a média alcançada.

mensagem = "calculadora de média (mas só funciona com 4 notas)"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

primeira_nota = float(input("Digite a primeira nota:  "))
segunda_nota = float(input("Digite a segunda nota:  "))
terceira_nota = float(input("Digite a terceira nota:  "))
quarta_nota = float(input("Digite a quarta nota:  "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print(f"\nP1: {primeira_nota}\nP2: {segunda_nota}\nP3: {terceira_nota}\nP4: {quarta_nota}")
print(f"\nA MÉDIA alcançada é de {media}")
