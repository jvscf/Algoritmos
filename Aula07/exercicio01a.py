n = int(input("Digite um número inteiro positivo: "))
e = 0
for i in range(1,n+1):
    e += 2 ** i
print(f"O Valor de E = {e:.2f}")