# Programa que calcule a multa pro excesso de kg de peixe

mensagem = "multa por excesso de peixe pescado"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

peso = float(input("Digite o peso total de peixes pescados:  "))
limite = 50
excesso = peso - limite
multa = 4
valor_multa = excesso * 4

if valor_multa <= 0:
    print(f"Com {peso}kg pescados não há multa")
else:
    print(f"Com {peso}kg pescados, a multa por excesso é de R${valor_multa:.2f}")

# Estrutura de condição utilizada
