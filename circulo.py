# Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

mensagem = "área de círcunferências"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

raio = float(input("Qual o raio da circunferência que deseja medir:  "))
area = math.pi * (raio**2)

print(f"\nA área de uma circunferência de raio igual a {raio} é {area:.2f}")
