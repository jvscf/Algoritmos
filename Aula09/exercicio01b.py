matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        n = int(input(f"Entre o valor para a posição ({i+1},{j+1}): "))
        linha.append(n)
    matriz.append(linha)
print(matriz[0][0])
print(matriz[0][1])
print(matriz[1][0])
print(matriz[1][1])