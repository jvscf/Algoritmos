vetor = []
for i in range(10):
    x = int(input(f"Digite o {i+1}o. valor: "))
    vetor.append(x)
maior = max(vetor)
for i in range(10):
    if vetor[i] == maior:
        print(f"O maior número é {maior} e sua posição é a {i+1}a.")