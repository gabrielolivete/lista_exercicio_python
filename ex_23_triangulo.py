#Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno

mensagem = "tipos de triângulos"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

lado_1 = float(input("Digite o tamanho do primeiro lado do triângulo:  "))
lado_2 = float(input("\nDigite o tamanho do segundo lado do triângulo:  "))
lado_3 = float(input("\nDigite o tamanho do terceiro lado do triângulo:  "))

if ((lado_1 + lado_2) > lado_3) and ((lado_1 + lado_3) > lado_2) and ((lado_2 + lado_3) > lado_1):
    print(f"""\nL1: {lado_1}
L2: {lado_2}
L3: {lado_3}

É um TRIÂNGULO\n""")
    if lado_1 == lado_2 == lado_3:
        print("Trata-se de um triângulo EQUILÁTERO.")
    elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
        print("Trata-se de um triângulo ISÓSCELES.")
    elif lado_1 != lado_2 != lado_3:
        print("Trata-se de um triângulo ESCALENO.")
    else:
        print("Impossível classificar.")
else:
    print("\nEssas medidas não formam um triângulo.")
