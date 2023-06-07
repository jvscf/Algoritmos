n = int(input("Digite um número inteiro positivo: "))
fat = 1
for i in range(1,n+1):
    fat *= i
print(fat)