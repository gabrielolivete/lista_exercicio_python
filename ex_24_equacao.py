#Programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from math import sqrt

mensagem = "equações de segundo grau"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

a = float(input("DIgite o valor de 'a':  "))

if a == 0:
    print(f"\na = {a:.0f} não caracteriza uma equação de segundo grau")
    exit()

b = float(input("Digite o valor de 'b':  "))
c = float(input("Digite o valor de 'c':  "))

delta = (b**2)-(4 * a * c)

raiz_delta = sqrt(delta)

x1 = ((-b) + raiz_delta) / (2 * a)

x2 = ((-b) - raiz_delta) / (2 * a)

if delta < 0:
    print(f"\nO valor de delta é igual a {delta:.2f}, ou seja, não possui raízes reais.")
elif delta == 0:
    print(f"\nO valor de delta é igual a {delta:.0f}, ou seja, possui apenas uma raíz real\nx = {x1:.2f}")
elif delta > 0:
    print(f"\nO valor de delta é igual a {delta:.2f}, ou seja, possui duas raízes reais\nx' = {x1:.2f}\nx'' = {x2:.2f}")
else:
    print("\nHá algo de errado no código.")
