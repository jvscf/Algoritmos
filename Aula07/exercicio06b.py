n = int(input("Digite um número inteiro positivo: "))
fat = 1
i = 1
while i <= n:
    fat *= i
    i += 1
print(fat)