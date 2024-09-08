# Prgrama que converte metros para centímetros.

mensagem = "conversor de medidas"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

metro = float(input("Digite qa medida em metros que deseja converter:  "))
centimetro = metro * 100

print(f"\nA medida de {metro}m equivale a {centimetro}cm")
