ra = input("Digite seu RA: ")
soma=0
mult=1
for i in range(0,len(ra)):
    soma += int(ra[i])
    mult *= int(ra[i])
print(soma)
print(mult)