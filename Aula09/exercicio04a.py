vetor = []
rotev = []
for i in range(20):
    x = str(input(f"Digite o {i+1}a. palavra de no máximo 10 caracteres: "))
    vetor.append(x)
    rotev.append(x[::-1])
print(rotev)