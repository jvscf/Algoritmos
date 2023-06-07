matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        n = int(input(f"Entre o valor para a posição ({i+1},{j+1}): "))
        linha.append(n)
    matriz.append(linha)
maior_elemento = matriz[0][0]
linha_maior_elemento = 0
coluna_maior_elemento = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] > maior_elemento:
            maior_elemento = matriz[linha][coluna]
            linha_maior_elemento = linha
            coluna_maior_elemento = coluna
print(maior_elemento)
print(linha_maior_elemento + 1)
print(coluna_maior_elemento + 1)
