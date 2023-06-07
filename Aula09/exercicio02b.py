matriz = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        matriz[i][j] = int(input(f"Entre o valor para a posição ({i+1},{j+1}): "))
maior = max(max(matriz))
mult = [[element * maior for element in row] for row in matriz]
print("Matriz resultante: ")
for row in mult:
    print(row)

