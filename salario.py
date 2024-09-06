# Programa que peça o valor ganho por hora trabalhada e o número de horas trabalhadas no mês para calcular o salário mensal.

mensagem = "calculadora de salário mensal"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

ganho_hora = float(input("Digite o valor ganho por hora trabalhada:  "))
horas = float(input("\nDigite as horas trabalhadas no mês:  "))

salario = ganho_hora * horas

print(f"\nTrabalhando {horas} horas e ganhando R${ganho_hora} por hora trabalhada, ao final do mês seu salário é de R${salario:.2f}")
