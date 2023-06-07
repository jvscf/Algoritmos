matriz = []
for i in range(8):
    linha = []
    for j in range(8):
        n = int(input(f"Entre o valor para a posição ({i+1},{j+1}): "))
        linha.append(n)
    matriz.append(linha)

cont = 0
for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == matriz[j][i]:
                cont += 1

if cont == 8**2:
    print("A matriz é simétrica")
else:
    print("A matriz não é simétrica")