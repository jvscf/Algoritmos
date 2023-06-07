matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
matrizt = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = float(input(f"Entre o valor para a posição ({i+1},{j+1}): "))
        matrizt[j][i] = matriz[i][j]
print(matriz)
print(matrizt)