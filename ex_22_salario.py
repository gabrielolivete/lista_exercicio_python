# Programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato, 10% para INSS e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%

mensagem = "descontos folha salarial"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

hora = int(input("Digite quantas horas você trabalhou no mês:  "))
valor = float(input("DIgite o valor de sua hora de trabalho:  "))

salario_bruto = hora * valor

ir_isento = salario_bruto * 0
ir_5 = salario_bruto * 0.05
ir_10 = salario_bruto * 0.10
ir_20 = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

descontos_fixos = inss + sindicato

if salario_bruto <= 900:
    print(f"""\nHoras trabalhadas: {hora}h
Valor/Hora: R${valor}

Salário Bruto: R${salario_bruto:.2f}

(-) IR (isento): R${ir_isento}
(-) INSS (10%): R${inss:.2f}
(-) Sindicato (3%): R${sindicato:.2f}
FGTS (11%): R${fgts:.2f}
Total de descontos: R${descontos_fixos:.2f}

Salário líquido: R${(salario_bruto - descontos_fixos):.2f}""")
elif 900 < salario_bruto <= 1500:
    print(f"""Horas trabalhadas: {hora}h
Valor/Hora: R${valor}

Salário Bruto: R${salario_bruto:.2f}

(-) IR (5%): R${ir_5}
(-) INSS (10%): R${inss:.2f}
(-) Sindicato (3%): R${sindicato:.2f}
FGTS (11%): R${fgts:.2f}
Total de descontos: R${(descontos_fixos + ir_5):.2f}

Salário líquido: R${(salario_bruto - descontos_fixos - ir_5):.2f}""")
elif 1500 < salario_bruto <= 2500:
    print(f"""Horas trabalhadas: {hora}h
Valor/Hora: R${valor}

Salário Bruto: R${salario_bruto:.2f}

(-) IR (10%): R${ir_10}
(-) INSS (10%): R${inss:.2f}
(-) Sindicato (3%): R${sindicato:.2f}
FGTS (11%): R${fgts:.2f}
Total de descontos: R${(descontos_fixos + ir_10):.2f}

Salário líquido: R${(salario_bruto - descontos_fixos - ir_10):.2f}""")
else:
    print(f"""Horas trabalhadas: {hora}h
Valor/Hora: R${valor}

Salário Bruto: R${salario_bruto:.2f}

(-) IR (20%): R${ir_20}
(-) INSS (10%): R${inss:.2f}
(-) Sindicato (3%): R${sindicato:.2f}
FGTS (11%): R${fgts:.2f}
Total de descontos: R${(descontos_fixos + ir_20):.2f}

Salário líquido: R${(salario_bruto - descontos_fixos - ir_20):.2f}""")
