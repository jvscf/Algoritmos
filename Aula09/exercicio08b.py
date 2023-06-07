matriz = []
somapar = 0
for i in range(5):
    linha = []
    for j in range(5):
        n = float(input(f"Entre o valor para a posição ({i+1},{j+1}): "))
        linha.append(n)
        if (i+1) % 2 == 0:
            somapar += n
    matriz.append(linha)

media = somapar / 10
print(media)
