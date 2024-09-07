# Programa que peça quanto o usuário ganha por hora e o número de horas trabalhadas e forneça um relatório com os descontos aplicados

mensagem = "folha salarial"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

valor_hora = float(input("Digite quanto você ganha por hora:  "))
hora_trabalhada = float(input("Digite quantas horas você trabalhou no mês:  "))

salario_bruto = valor_hora * hora_trabalhada
ir = 0.11
desc_ir = salario_bruto * ir
inss = 0.08
desc_inss = salario_bruto * inss
sind = 0.05
desc_sind = salario_bruto * sind
salario_liquido = salario_bruto - desc_ir - desc_inss - desc_sind

print(f"""\nFOLHA SALARIAL
    + Salário Bruto: R$ {salario_bruto:.2f}
    - IR (11%): R$ {desc_ir:.2f}
    - INSS (8%): R$ {desc_inss:.2f}
    - Sindicato (5%): R$ {desc_sind:.2f}
    
    = Salário líquido: R$ {salario_liquido:.2f}""")
