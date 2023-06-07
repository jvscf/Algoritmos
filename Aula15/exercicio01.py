with open("usuarios.txt") as arquivo:
    texto = arquivo.read()
    lista = texto.split("\n")

    linha = []
    dic = {}
    soma = 0.0
    for itens in lista:
        linha = itens.split(",")
        dic[linha[0]] = int(linha[1])/(1024*1024)
        soma += dic[linha[0]]

    media = soma / 6

print("ACME Inc.                    Uso do espaço em disco pelos usuários\n")
print("-------------------------------------------------------------------------")
print("Nr.   Usuario               Espaço ultilizado     % do uso")
item = 0

for nome, espaco in dic.items():
    branconome = len(nome)-15
    item += 1
    print(f"{item}     {nome}      {espaco:.2f} MB      {(espaco/soma)*100:.2f}%")

print(f"\n\nEspaço total ocupado: {soma:.2f}MB")
print(f"Espaço medio ocupado: {media:.2f}MB")
