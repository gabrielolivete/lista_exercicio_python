# Programa que receba duas notas parciais de um aluno e calcule a média. O programa deve informar se o aluno está aprovado ou reprovado

mensagem = "boletim escolar"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

media = int(input("Digite a média de aprovação na sua escola:  "))
recuperacao = int(input("Digite a nota mínima para realizar prova de recuperação:  "))
nota_1 = float(input("\nDigite sua nota da primeira prova:  "))
nota_2 = float(input("Digite sua nota da segunda prova:  "))

calculo_media = (nota_1 + nota_2) / 2

if calculo_media >= media:
    print(f"\nParabéns, você foi aprovado com {calculo_media:.2f}")
elif media > calculo_media >= recuperacao:
    print(f"\nVocê ainda tem uma chance, você vai para recuperação com {calculo_media}")
else:
    print(f"\nInfelizmente {calculo_media} não é suficiente para ser aprovado(a)")
