# Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo

mensagem = "leitura de números"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

numero = int(input("Digite um número inteiro entre 1 e 1000:  "))

if numero > 1000 or numero < 0:
    print("\nNúmero fora do intervalo")
    exit()

unidades = numero % 10
dezenas = (numero // 10) % 10
centenas = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f"O número {numero} contém:\n")

if milhar > 0:
    print(f"{milhar} milhar")

if centenas == 1:
    print(f"{centenas} centena")
elif centenas > 1:
    print(f"{centenas} centenas")

if dezenas == 1:
    print(f"{dezenas} dezena")
elif dezenas > 1:
    print(f"{dezenas} dezenas")

if unidades == 1:
    print(f"{unidades} unidade")
elif unidades > 1:
    print(f"{unidades} unidades")
