matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
soma = 0
for i in range(4):
    for j in range(4):
        matriz[i][j] = float(input(f"Entre o valor para a posição ({i+1},{j+1}): "))
        if i == j:
            soma += matriz[i][j]
print(matriz)
print(soma)