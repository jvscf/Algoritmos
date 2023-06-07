nome = input("Digite seu nome: ")
novo_nome = ""
for i in range(0, len(nome)):
    letra = nome[i]
    nova_letra = chr(ord(letra) + 1)
    novo_nome += nova_letra
print(novo_nome)