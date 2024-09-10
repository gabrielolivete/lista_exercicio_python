# Programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 1280,00 (incluindo) : aumento de 20%
# salários entre R$ 1280,00 e R$ 1700,00 : aumento de 15%
# salários entre R$ 1700,00 e R$ 2300,00 : aumento de 10%
# salários de R$ 2300,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

mensagem = "aumento folha salarial"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

salario = float(input("Digite seu salário atual:  "))

if salario <= 1280:
    print(f"\nSeu salário atual de R${salario} receberá um aumento de 20%, seu novo salário é de R${(salario * 1.20):.2f}")
elif 1280 < salario <= 1700:
    print(f"\nSeu salário atual de R${salario} receberá um aumento de 15%, seu novo salário é de R${(salario * 1.15):.2f}")
elif 1700 < salario <= 2300:
    print(f"\nSeu salário atual de R${salario} receberá um aumento de 10%, seu novo salário é de R${(salario * 1.10):.2f}")
else:
    print(f"\nSeu salário atual de R${salario} receberá um aumento de 5%, seu novo salário é de R${(salario * 1.05):.2f}")
