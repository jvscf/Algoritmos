e = 0
n = int(input("Digite um número inteiro positivo: "))
b = int(input("Digite o valor da base: "))
i = 1
while i <= n:
    e += b ** i
    i += 1
print(f"O valor de E é {e:.2f}")
