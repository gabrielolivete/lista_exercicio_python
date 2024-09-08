# Programa que peça o tamanho de um arquivo para download e velocidade de internet para calcular o tempo aproximado de download

mensagem = "tempo de download"
print(len(mensagem) * "=")
print(mensagem.upper())
print(len(mensagem) * "=", "\n")

arquivo = int(input("Digite quantos MB possui o arquivo:  "))
velocidade = int(input("\nDigite a velocidade em Mbps da sua internet:  "))

download = arquivo / velocidade
min = download // 60
resto = (download / 60) - min
seg = resto * 60

if download < 60:
    print(f"\nCom uma conexão de {velocidade}Mbps, seu arquivo de {arquivo}MB será baixado em {download}s")
else:
    print(f"\nCom uma conexão de {velocidade}Mbps, seu arquivo de {arquivo}MB será baixado em {round(min)}min e {round(seg)}s")
