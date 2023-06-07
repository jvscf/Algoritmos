vetor = []
for i in range(10):
    x = int(input(f"Digite o {i+1}o. valor: "))
    vetor.append(x)
print(vetor[::-1])
vetor.reverse()
print(vetor)