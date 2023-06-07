matriz = []
for i in range(10):
    linha = []
    for j in range(20):
        n = int(input(f"Entre o valor para a posição ({i+1},{j+1}): "))
        linha.append(n)
    matriz.append(linha)
somas = []
for linha in matriz:
    soma = sum(linha)
    somas.append(soma)
print(somas)
for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] *= somas[i]
print(matriz)