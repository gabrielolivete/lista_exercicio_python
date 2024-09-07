# Programa que receba a altura de uma pessoa e calcule seu peso ideal a partir de uma fórmula

mensagem = "calcule seu peso ideal"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

altura = float(input("Digite sua altura em metros (ex: 1.62):  "))
peso_ideal_m = (62.1 * altura) - 44.7
peso_ideal_h = (72.7 * altura) - 58

print(f"\nMULHER\nCom uma altura de {altura}m seu peso ideal é aproximadamente {round(peso_ideal_m)}kg")
print(f"\nHOMEM\nCom uma altura de {altura}m seu peso ideal é aproximadamente {round(peso_ideal_h)}kg")
