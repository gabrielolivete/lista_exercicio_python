# Programa que peça a temperatura em graus Celsius e transforme para graus Farenheit.

mensagem = "conversor de temperatura"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

celsius = float(input("Digite a temperatura em graus Celsius:  "))
faren = (celsius * 1.8) + 32

print(f"\nA temperatura de {celsius}°C equivale a {faren:.2f}°F")
