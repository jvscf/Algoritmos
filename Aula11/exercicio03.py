l1 = []
l2 = []

for i in range(10):
    x = int(input(f"Digite o {i + 1}o. número inteiro da primeira lista: "))
    l1.append(x)
    y = int(input(f"Digite o {i + 1}o. número inteiro da segunda lista: "))
    l2.append(y)

c1 = set(l1)
c2 = set(l2)
cun = c1.union(c2)
print(cun)