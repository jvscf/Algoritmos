idades={}
soma=0
media = 0
for nome in range(5):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    idades[nome] = idade
    soma += idade
    media = soma / 5
    print(idades)
for nome, idade in idades.items():
    if idade > media:
        print(f"{nome} tem {idade} anos!")