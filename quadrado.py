# Programa que calcule a área de um quadrado e em seguida mostre o dobro da área para o usuário.

mensagem = "área quadrada"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

lado = float(input("Digite a medida do lado do quadrado que deseja medir a área (em metros):  "))
area = lado**2
dobro_area = area * 2

print(f"\nA área de um quadrado de lado igual a {lado}m é de {area}m² e o dobro dessa área é igual a {dobro_area}m²")
