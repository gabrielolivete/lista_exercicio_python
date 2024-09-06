# Programa que peça a temperatura em graus Farenheit e transforme para graus Celsius.

mensagem = "temperatura de americano"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

faren = float(input("Está nos EUA? Digite a temperatura em graus Farenheit:  "))
celsius = 5 * ((faren - 32) / 9)

print(f"\nA temperatura de {faren}°F equivale a {celsius:.2f}°C")
