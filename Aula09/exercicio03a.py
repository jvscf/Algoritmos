v1 = [0]*10
v2 = [0]*10
v3 = []
for i in range(10):
    v1[i] = int(input(f"Digite o {i+1}o. elemento do vetor 1: "))
    v2[i] = int(input(f"Digite o {i+1}o. elemento do vetor 2: "))
    v3.append(v1[i])
    v3.append(v2[i])
print(v3)